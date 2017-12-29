from flask import *

from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kgisl@localhost/onlineacc'
app.config['SECRET_KEY'] = "random string"


db = SQLAlchemy(app)

	
@app.route("/")
def index():
	return render_template("loginonline.html")
	
@app.route("/login")
def login():
	return render_template("loginonline.html")
	
@app.route("/register")
def register():
	return render_template("register.html")
	
@app.route("/elementary")
def elementary():
	return render_template("elementary.html")
	
@app.route("/primary")
def primary():
	return render_template("primary.html")
	
@app.route("/secondary")
def secondary():
	return render_template("secondary.html")
	
@app.route("/higher_secondary")
def higher_secondary():
	return render_template("higher_secondary.html")
	
@app.route("/contact")
def contact():
	return render_template("contact.html")
	
class register(db.Model):
	id=db.Column('student_id',db.Integer,primary_key=True)
	first_name=db.Column(db.String)
	last_name=db.Column(db.String)
	display_name=db.Column(db.String)
	email_address=db.Column(db.String)
	password=db.Column(db.String)
	confirm_password=db.Column(db.String)
		
	def __init__(self,first_name,last_name,display_name,email_address,password,confirm_password):
		self.first_name=first_name
		self.last_name=last_name
		self.display_name=display_name
		self.email_address=email_address
		self.password=password
		self.confirm_password=confirm_password
		
	@app.route("/register_db",methods=["GET","POST"])
	def register_db():
		if request.method == 'POST':
			if not request.form['first_name'] or not request.form['last_name'] or not request.form['display_name'] or not request.form['email_address'] or not request.form['password'] or not request.form['confirm_password']:
				flash("Error")
			else:
				student=register(request.form['first_name'],request.form['last_name'],request.form['display_name'],request.form['email_address'],request.form['password'],request.form['confirm_password'])
				db.session.add(student)
				db.session.commit()
			return redirect(url_for('register'))
		return render_template("register.html")
		
class elementary(db.Model):
	id=db.Column('student_id',db.Integer,primary_key=True)
	standard=db.Column(db.String)
	staff=db.Column(db.String)
	classes=db.Column(db.String)
	ground=db.Column(db.String)
	washrooms=db.Column(db.String)	
	
	def __init__(self,standard,staff,classes,ground,washrooms):
		self.standard=standard
		self.staff=staff
		self.classes=classes
		self.ground=ground
		self.washrooms=washrooms

	@app.route("/elementary_db",methods=["GET","POST"])
	def elementary_db():
		if request.method == 'POST':
			if not request.form['standard'] or not request.form['staff'] or not request.form['classes'] or not request.form['ground'] or not request.form['washrooms']:
				flash("Error")
			else:
				student=elementary(request.form['standard'],request.form['staff'],request.form['classes'],request.form['ground'],request.form['washrooms'])
				db.session.add(student)
				db.session.commit()
			return redirect(url_for('elementary'))
		return render_template("elementary.html")
	
class primary(db.Model):
	id=db.Column('student_id',db.Integer,primary_key=True)
	standard=db.Column(db.String)
	staff=db.Column(db.String)
	classes=db.Column(db.String)
	ground=db.Column(db.String)
	washrooms=db.Column(db.String)	
	
	def __init__(self,standard,staff,classes,ground,washrooms):
		self.standard=standard
		self.staff=staff
		self.classes=classes
		self.ground=ground
		self.washrooms=washrooms

	@app.route("/primary_db",methods=["GET","POST"])
	def primary_db():
		if request.method == 'POST':
			if not request.form['standard'] or not request.form['staff'] or not request.form['classes'] or not request.form['ground'] or not request.form['washrooms']:
				flash("Error")
			else:
				student=primary(request.form['standard'],request.form['staff'],request.form['classes'],request.form['ground'],request.form['washrooms'])
				db.session.add(student)
				db.session.commit()
			return redirect(url_for('primary'))
		return render_template("primary.html")
	
class secondary(db.Model):
	id=db.Column('student_id',db.Integer,primary_key=True)
	Standard=db.Column(db.String)
	Staff=db.Column(db.String)
	Classes=db.Column(db.String)
	Ground=db.Column(db.String)
	Computer=db.Column(db.String)	
	Science=db.Column(db.String)	
	wash_rooms=db.Column(db.String)	
	
	def __init__(self,Standard,Staff,Classes,Ground,Computer,Science,wash_rooms):
		self.Standard=Standard
		self.Staff=Staff
		self.Classes=Classes
		self.Ground=Ground
		self.Computer=Computer
		self.Science=Science
		self.wash_rooms=wash_rooms

	@app.route("/secondary_db",methods=["GET","POST"])
	def secondary_db():
		if request.method == 'POST':
			if not request.form['Standard'] or not request.form['Staff'] or not request.form['Classes'] or not request.form['Ground'] or not request.form['Computer'] or not request.form['Science'] or not request.form['wash_rooms']:
				flash("Error")
			else:
				student=secondary(request.form['Standard'],request.form['Staff'],request.form['Classes'],request.form['Ground'],request.form['Computer'],request.form['Science'],request.form['wash_rooms'])
				db.session.add(student)
				db.session.commit()
			return redirect(url_for('secondary'))
		return render_template("secondary.html")
		return render_template("primary.html")
	
class higher_secondary(db.Model):
	id=db.Column('student_id',db.Integer,primary_key=True)
	Standard=db.Column(db.String)
	Staff=db.Column(db.String)
	Classes=db.Column(db.String)
	Ground=db.Column(db.String)
	Computer=db.Column(db.String)	
	physics=db.Column(db.String)	
	Science=db.Column(db.String)	
	wash_rooms=db.Column(db.String)	
	
	def __init__(self,Standard,Staff,Classes,Ground,Computer,physics,Biology,chemistry,wash_rooms):
		self.Standard=Standard
		self.Staff=Staff
		self.Classes=Classes
		self.Ground=Ground
		self.Computer=Computer
		self.physics=physics
		self.Biology=Biology
		self.chemistry=chemistry		
		self.wash_rooms=wash_rooms

	@app.route("/higher_secondary_db",methods=["GET","POST"])
	def higher_secondary_db():
		if request.method == 'POST':
			if not request.form['Standard'] or not request.form['Staff'] or not request.form['Classes'] or not request.form['Ground'] or not request.form['Computer'] or not request.form['physics'] or not request.form['Biology'] or not request.form['chemistry'] or not request.form['wash_rooms']:
				flash("Error")
			else:
				student=higher_secondary(request.form['Standard'],request.form['Staff'],request.form['Classes'],request.form['Ground'],request.form['Computer'],request.form['physics'],request.form['Biology'],request.form['chemistry'],request.form['wash_rooms'])
				db.session.add(student)
				db.session.commit()
			return redirect(url_for('higher_secondary'))
		return render_template("higher_secondary.html")
	
class contact(db.Model):
	id=db.Column('student_id',db.Integer,primary_key=True)
	Standard=db.Column(db.String)
	Staff=db.Column(db.String)
	Classes=db.Column(db.String)
	Ground=db.Column(db.String)
	
	def __init__(self,Standard,Staff,Classes,Ground):
		self.Standard=Standard
		self.Staff=Staff
		self.Classes=Classes
		self.Ground=Ground

	@app.route("/contact_db",methods=["GET","POST"])
	def contact_db():
		if request.method == 'POST':
			if not request.form['Standard'] or not request.form['Staff'] or not request.form['Classes'] or not request.form['Ground']:
				flash("Error")
			else:
				student=contact(request.form['Standard'],request.form['Staff'],request.form['Classes'],request.form['Ground'])
				db.session.add(student)
				db.session.commit()
			return redirect(url_for('contact'))
		return render_template("contact.html")
		
if __name__=='__main__':
	db.create_all()
	app.run(debug = True)

