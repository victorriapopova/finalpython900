from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Service, Review


# Home page route
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# Services page route
@app.route('/services')
def services():
    services2 = Service.query.all()
    return render_template('services.html', services=services2)


# Reviews page route
# noinspection PyShadowingNames
@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    if request.method == 'POST':
        name = request.form.get('name')
        review_text = request.form.get('review')
        new_review = Review(name=name, review_text=review_text)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('reviews'))

    reviews = Review.query.all()
    return render_template('reviews.html', reviews=reviews)


# Contact page route
@app.route('/contact')
def contact():
    return render_template('contact.html')


# Error handler for 404 Not Found
@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404


# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error():
    db.session.rollback()  # Rollback any database session changes
    return render_template('500.html'), 500
