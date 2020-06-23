from flask import Flask, render_template, request, redirect
import csv
import mysql.connector

app = Flask(__name__)
print(__name__)


@app.route('/')
def myweb():
    return render_template('index.html')


@app.route('/<string:page_input>')
def html_page(page_input):
    return render_template(page_input)


def write_to_file(data):
    with open('database.txt', mode='a')as database:
        email = data['email']
        subject = data['subject']
        message = data['message']

        file = database.write(f'\n{email}, {subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='')as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # with open('database.csv', 'r')as rd:
        #     read = csv.reader(database2, delimiter=' ', quotechar='|')
        #     for row[0] in read:
        #         csv_writer.writerow(['Email','Subject','Message'])

        # csv_writer.writerow(['email', 'subject', 'message'])
        # csv_writer.writerow([email, subject, message])
        write = csv_writer.writerow([email, subject, message])


def conection(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='', database='db')
    mycursor = mydb.cursor()
    mycursor.execute('insert into contact_data(email,subject,message) values  (%s,%s,%s)',(email,subject,message))
    mydb.commit()
    # print('sucessfull')



@app.route('/submit_form', methods=['GET', 'POST'])
def submited_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
#         conection(data)
        # print(data)
        return redirect('/thankyou.html')
    else:
        return 'Please check and retry'

# @app.route('/index.html')
# def home():
#     return render_template('index.html')
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/work.html')
# def work ():
#     return render_template('work.html')
#
# @app.route('/works.html')
# def works ():
#     return render_template('works.html')
#
# @app.route('/contact.html')
# def contact ():
#     return render_template('contact.html')
# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# @app.route('/blog')
# def blog():
#     return 'Hello, Diptak Sengupta u r master in web developments all parts will come here'
