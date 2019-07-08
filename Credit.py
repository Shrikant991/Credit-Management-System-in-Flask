from flask import Flask,render_template,flash,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField,SubmitField,StringField
from flask_sqlalchemy import SQLAlchemy
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired,ValidationError
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SECRET_KEY']='random'

db=SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False)
    email = db.Column(db.String(120), unique=False)
    credit = db.Column(db.Integer, primary_key=False)

    def __init__(self, username, email, credit):
        self.username = username
        self.email = email
        self.credit = credit


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sentby = db.Column(db.String(20), unique=False)
    recievedby = db.Column(db.String(20), unique=False)
    transfer = db.Column(db.Integer, primary_key=False,nullable=False)

    def __init__(self, sentby, recievedby, transfer):
        self.sentby = sentby
        self.recievedby = recievedby
        self.transfer = transfer


class TransferForm(FlaskForm):
    user= StringField('Transfer Credit To',validators=[DataRequired(),ValidationError])
    transfer = IntegerField('Transfer Credit',validators=[DataRequired()])
    submit=SubmitField('Transfer')

def validate_user(self,user):
    #form=TransferForm()
    user_object=Person.query.filter_by(username=user.data).first()
    if user_object==None:
        raise ValidationError('User doesnt Exist!')


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
 

@app.route("/users")
def Users():
    persons = Person.query.all()
    return render_template('users.html', myPersons=persons)

@app.route("/user1",methods=['GET', 'POST'])
def Users1():
    form=TransferForm()
    if form.validate_on_submit():
        trans = Transactions(sentby='User1', recievedby=form.user.data, transfer=form.transfer.data)
        db.session.add(trans)
        db.session.commit()
        persons = Person.query.filter_by(username='User1').first()
        persons.credit=persons.credit-form.transfer.data
        db.session.commit()
        persons = Person.query.filter_by(username=form.user.data).first()
        persons.credit=persons.credit+form.transfer.data
        db.session.commit()
        flash(f'Credit Transfered!', 'success')
        return redirect(url_for('home'))
    persons = Person.query.filter_by(username='User1').first()
    return render_template('accounts.html', myPersons=persons,form=form)

@app.route("/user2",methods=['GET', 'POST'])
def Users2():
    form=TransferForm()
    if form.validate_on_submit():
        trans = Transactions(sentby='User2', recievedby=form.user.data, transfer=form.transfer.data)
        db.session.add(trans)
        db.session.commit()
        persons = Person.query.filter_by(username='User2').first()
        persons.credit=persons.credit-form.transfer.data
        db.session.commit()
        persons = Person.query.filter_by(username=form.user.data).first()
        persons.credit=persons.credit+form.transfer.data
        db.session.commit()
        flash(f'Credit Transfered!', 'success')
        return redirect(url_for('home'))
    persons = Person.query.filter_by(username='User2').first()
    return render_template('accounts.html', myPersons=persons,form=form)

@app.route("/user3",methods=['GET', 'POST'])
def Users3():
    form=TransferForm()
    if form.validate_on_submit():
        trans = Transactions(sentby='User3', recievedby=form.user.data, transfer=form.transfer.data)
        db.session.add(trans)
        db.session.commit()
        persons = Person.query.filter_by(username='User3').first()
        persons.credit=persons.credit-form.transfer.data
        db.session.commit()
        persons = Person.query.filter_by(username=form.user.data).first()
        persons.credit=persons.credit+form.transfer.data
        db.session.commit()
        flash(f'Credit Transfered!', 'success')
        return redirect(url_for('home'))
    persons = Person.query.filter_by(username='User3').first()
    return render_template('accounts.html', myPersons=persons,form=form)

@app.route("/user4",methods=['GET', 'POST'])
def Users4():
    form=TransferForm()
    if form.validate_on_submit():
        trans = Transactions(sentby='User4', recievedby=form.user.data, transfer=form.transfer.data)
        db.session.add(trans)
        db.session.commit()
        persons = Person.query.filter_by(username='User4').first()
        persons.credit=persons.credit-form.transfer.data
        db.session.commit()
        persons = Person.query.filter_by(username=form.user.data).first()
        persons.credit=persons.credit+form.transfer.data
        db.session.commit()
        flash(f'Credit Transfered!', 'success')
        return redirect(url_for('home'))
    persons = Person.query.filter_by(username='User4').first()
    return render_template('accounts.html', myPersons=persons,form=form)

@app.route("/user5",methods=['GET', 'POST'])
def Users5():
    form=TransferForm()
    if form.validate_on_submit():
        trans = Transactions(sentby='User5', recievedby=form.user.data, transfer=form.transfer.data)
        db.session.add(trans)
        db.session.commit()
        persons = Person.query.filter_by(username='User5').first()
        persons.credit=persons.credit-form.transfer.data
        db.session.commit()
        persons = Person.query.filter_by(username=form.user.data).first()
        persons.credit=persons.credit+form.transfer.data
        db.session.commit()
        flash(f'Credit Transfered!', 'success')
        return redirect(url_for('home'))
    persons = Person.query.filter_by(username='User5').first()
    return render_template('accounts.html', myPersons=persons,form=form)

@app.route("/user6",methods=['GET', 'POST'])
def Users6():
    form=TransferForm()
    if form.validate_on_submit():
        trans = Transactions(sentby='User6', recievedby=form.user.data, transfer=form.transfer.data)
        db.session.add(trans)
        db.session.commit()
        persons = Person.query.filter_by(username='User6').first()
        persons.credit=persons.credit-form.transfer.data
        db.session.commit()
        persons = Person.query.filter_by(username=form.user.data).first()
        persons.credit=persons.credit+form.transfer.data
        db.session.commit()
        flash(f'Credit Transfered!', 'success')
        return redirect(url_for('home'))
    persons = Person.query.filter_by(username='User6').first()
    return render_template('accounts.html', myPersons=persons,form=form)


@app.route("/user7",methods=['GET', 'POST'])
def Users7():
    form=TransferForm()
    if form.validate_on_submit():
        trans = Transactions(sentby='User7', recievedby=form.user.data, transfer=form.transfer.data)
        db.session.add(trans)
        db.session.commit()
        persons = Person.query.filter_by(username='User7').first()
        persons.credit=persons.credit-form.transfer.data
        db.session.commit()
        persons = Person.query.filter_by(username=form.user.data).first()
        persons.credit=persons.credit+form.transfer.data
        db.session.commit()
        flash(f'Credit Transfered!', 'success')
        return redirect(url_for('home'))
    persons = Person.query.filter_by(username='User7').first()
    return render_template('accounts.html', myPersons=persons,form=form)

@app.route("/user8",methods=['GET', 'POST'])
def Users8():
    form=TransferForm()
    if form.validate_on_submit():
        trans = Transactions(sentby='User8', recievedby=form.user.data, transfer=form.transfer.data)
        db.session.add(trans)
        db.session.commit()
        persons = Person.query.filter_by(username='User8').first()
        persons.credit=persons.credit-form.transfer.data
        db.session.commit()
        persons = Person.query.filter_by(username=form.user.data).first()
        persons.credit=persons.credit+form.transfer.data
        db.session.commit()
        flash(f'Credit Transfered!', 'success')
        return redirect(url_for('home'))
    persons = Person.query.filter_by(username='User8').first()
    return render_template('accounts.html', myPersons=persons,form=form)

@app.route("/user9",methods=['GET', 'POST'])
def Users9():
    form=TransferForm()
    if form.validate_on_submit():
        trans = Transactions(sentby='User9', recievedby=form.user.data, transfer=form.transfer.data)
        db.session.add(trans)
        db.session.commit()
        persons = Person.query.filter_by(username='User9').first()
        persons.credit=persons.credit-form.transfer.data
        db.session.commit()
        persons = Person.query.filter_by(username=form.user.data).first()
        persons.credit=persons.credit+form.transfer.data
        db.session.commit()
        flash(f'Credit Transfered!', 'success')
        return redirect(url_for('home'))
    persons = Person.query.filter_by(username='User9').first()
    return render_template('accounts.html', myPersons=persons,form=form)

@app.route("/user10",methods=['GET', 'POST'])
def Users10():
    form=TransferForm()
    if form.validate_on_submit():
        trans = Transactions(sentby='User10', recievedby=form.user.data, transfer=form.transfer.data)
        db.session.add(trans)
        db.session.commit()
        persons = Person.query.filter_by(username='User10').first()
        persons.credit=persons.credit-form.transfer.data
        db.session.commit()
        persons = Person.query.filter_by(username=form.user.data).first()
        persons.credit=persons.credit+form.transfer.data
        db.session.commit()
        flash(f'Credit Transfered!', 'success')
        return redirect(url_for('home'))
    persons = Person.query.filter_by(username='User10').first()
    return render_template('accounts.html', myPersons=persons,form=form)


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/transactions")
def transactions():
    persons = Transactions.query.all()
    return render_template('transactions.html',myPersons=persons)
    

if __name__ == '__main__':
	app.run(debug=True)