from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Admin(db.Model):
    __tablename__ = 'Admin'
    Admin_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), nullable=False)
    Password = db.Column(db.String(100), nullable=False)

class Donations(db.Model):
    __tablename__ = 'Donations'
    Donation_ID = db.Column(db.Integer, primary_key=True, nullable=False)
    Donor_ID = db.Column(db.Integer, nullable=False)
    Ngo_ID = db.Column(db.Integer, nullable=False)
    Req_ID = db.Column(db.Integer, nullable=False)
    Item = db.Column(db.String(100), nullable=False)
    Quantity_Amount = db.Column(db.Integer, nullable=False)
    Timestamp = db.Column(db.TIMESTAMP, nullable=False)

class Donors(db.Model):
    __tablename__ = 'Donors'
    Donor_ID = db.Column(db.Integer, primary_key=True, nullable=False)
    Timestamp = db.Column(db.TIMESTAMP, nullable=False)

class Ngos(db.Model):
    __tablename__ = 'Ngos'
    Ngo_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), nullable=False)
    Password = db.Column(db.String(100), nullable=False)
    Contact = db.Column(db.Integer, nullable=False)

class Requirements_History(db.Model):
    __tablename__ = 'Requirements_History'
    ReqID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    Ngo_Name = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), nullable=False)
    Requirement = db.Column(db.Integer, nullable=False)
    Quantity_Amount = db.Column(db.Integer, nullable=False)
    Other_Details = db.Column(db.String(200), nullable=False)
    Status = db.Column(db.String(100), nullable=False, default='Pending', collation='UTF16CI')
    Timestamp = db.Column(db.TIMESTAMP, nullable=False)

class Requirements_Updated(db.Model):
    __tablename__ = 'Requirements_Updated'
    ReqID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    Ngo_Name = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), nullable=False)
    Requirement = db.Column(db.Integer, nullable=False)
    Quantity_Amount = db.Column(db.Integer, nullable=False)
    Other_Details = db.Column(db.String(200), nullable=False)
    Status = db.Column(db.String(100), nullable=False, default='Pending', collation='UTF16CI')
    Timestamp = db.Column(db.TIMESTAMP, nullable=False)

class Users(db.Model):
    __tablename__ = 'Users'
    User_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), nullable=False)
    Password = db.Column(db.String(100), nullable=False)
    Contact = db.Column(db.Integer, nullable=False)
