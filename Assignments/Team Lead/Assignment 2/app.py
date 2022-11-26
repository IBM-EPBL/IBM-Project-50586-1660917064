from flask import Flask,render_template,request
import DB2 as db

app = Flask(__name__)


# @app.route('/',methods =['GET', 'POST']) 
# def login():
#     global userid
#     msg = ''
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         sql = "SELECT * FROM USERS WHERE EMAIL=? AND PASSWORD=?"
#         stmt = ibm_db.prepare(conn,sql)
#         ibm_db.bind_param(stmt,1,email)
#         ibm_db.bind_param(stmt,2,password)
#         ibm_db.execute(stmt)
#         res = ibm_db.fetch_assoc(stmt)
#         print(res)
#         if res:
#             session['loggedin'] = True
#             session['id'] = res['USERNAME']
#             userid = res['USERNAME']
#             session['username'] = res['USERNAME']
#             msg = res['USERNAME']
        
#             return render_template('dashboard.html', msg = msg)
#         else:
#             msg = "Incorrect username/password!!"
#             return render_template('login.html', msg = msg) 

# @app.route('/register',methods =['GET', 'POST']) 
# def register(): 
#     msg = ''
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']
#         sql = "SELECT * FROM USERS WHERE USERNAME=?"
#         stmt = ibm_db.prepare(conn,sql)
#         ibm_db.bind_param(stmt,1,username)
#         ibm_db.execute(stmt)
#         res = ibm_db.fetch_assoc(stmt)
#         print(res)
#         if res:
#             msg = "Account already exists !!"
#         elif not re.match(r'[^@]+@[^@]+\.[^@]+',email):
#             msg = "Invalid Email address"
#         elif not re.match(r'[A-Za-z0-9]+',username):
#             msg = "Name must contain only characters and numbers !!"
#         else:
#             sql = "INSERT INTO USERS VALUES (?,?,?)"
#         stmt = ibm_db.prepare(conn,sql)
#         ibm_db.bind_param(stmt,1,username)
#         ibm_db.bind_param(stmt,2,email)
#         ibm_db.bind_param(stmt,3,password)
#         ibm_db.execute(stmt)
#         msg = "Successgully registered !!Login to continue"
#         return render_template('login.html', msg = msg)
#     elif request.method == 'POST':
#         msg = "Please fill out the form !"
#         return render_template('register.html', msg = msg)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/login", methods=['POST'])
def CheckLogin():
    print(request.form['username'])
    print(request.form['password'])
    return render_template('home.html')

@app.route("/create_user",methods=['GET'])
def register():
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)