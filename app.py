from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newborn_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Feeding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    duration = db.Column(db.Integer, nullable=False)

class Sleep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    duration = db.Column(db.Integer, nullable=False)

class Diaper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    type = db.Column(db.String(10), nullable=False)

# Ensure tables are created before the first request
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    feedings = Feeding.query.order_by(Feeding.time.desc()).all()
    sleep = Sleep.query.order_by(Sleep.time.desc()).all()
    diapers = Diaper.query.order_by(Diaper.time.desc()).all()
    return render_template('index.html', feedings=feedings, sleep=sleep, diapers=diapers)

@app.route('/log', methods=['POST'])
def log():
    event_type = request.form['type']
    if event_type == 'feeding':
        duration = request.form['duration']
        event = Feeding(duration=duration)
    elif event_type == 'sleep':
        duration = request.form['duration']
        event = Sleep(duration=duration)
    elif event_type == 'diaper':
        diaper_type = request.form['diaper_type']
        event = Diaper(type=diaper_type)

    db.session.add(event)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
