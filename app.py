from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

df = pd.read_csv('students_database.csv')


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/high')
def view_topper():
   
    topper = df.loc[df['Marks'].idxmax()]
    #return render_template('maxi.html', high=highest)
    return render_template('maxi.html', name=topper['Name'], marks=topper['Marks'])

@app.route('/search', methods=['POST'])
def search():
    # Load the Excel file into a Pandas DataFrame
   # df = pd.read_excel('students_database.xlsx')

    # Retrieve the user's input from the form
    name_to_search = request.form['name']

    # Filter the DataFrame to find rows where the 'Name' column matches the input name
    search_results = df[df['Name'] == name_to_search]

    # Render the search results in an HTML template
    return render_template('search_results.html', results=search_results)

@app.route('/average')
def average():
    # Read the Excel sheet into a pandas DataFrame

    # Calculate the average marks of all students
    avg_marks = df['Marks'].mean()

    # Render the HTML template with the average marks
    return render_template('average.html', avg_marks=avg_marks)

@app.route('/failed')
def failed():
    
#failed students list
    failed_students = df[df['Result'] == 'FAIL']['Name'].tolist()
    return render_template('failed.html', failed_students = failed_students)

@app.route('/passed')
def passed():
    
#failed students list
    passed_students = df[df['Result'] == 'PASS']['Name'].tolist()
    return render_template('passed.html', passed_students = passed_students)

@app.route('/OtherData')
def OtherData(): 
    desc = df.describe()
    return render_template('otherData.html', desc=desc.to_html())

class StudentNotFound(Exception):
    pass

@app.errorhandler(StudentNotFound)
def handle_student_not_found_error(error):
    return redirect(url_for('index')), 302


if __name__ == '__main__':
    app.run(debug=True)
