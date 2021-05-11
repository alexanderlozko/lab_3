from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yutqtwawqkjdnc:671881f90b94cf097728248eb4af95fcbabcf0b10e65bba4cd16c800e9600106@ec2-54-163-254-204.compute-1.amazonaws.com:5432/d5ecfb0jn6uicb'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:my_password@localhost:54320/lab3'
db = SQLAlchemy(app)

class Brand(db.Model):
    name = db.Column(db.String(64), primary_key=True)
    year = db.Column(db.Integer, index=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    price = db.Column(db.Integer)
    brand = db.Column(db.String(64), db.ForeignKey('brand.name'))


db.create_all()
db.session.commit()


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    message = ''

    brand_posts = Brand.query.all()
    product_posts = Product.query.all()

    if request.method == 'POST':
        brand = request.form.get('name_brand')
        year = request.form.get('year_brand')
        #проверки на год нет
        if brand and year != '':
            add = Brand(name=brand, year=year)
            db.session.add(add)
            db.session.commit()
            #message = 'brand was added'
            return redirect('index')


        # try:
        #     db.session.add(add)
        #     db.session.commit()
        # except Exception:
        #     message = 'Error'


        product = request.form.get('name_product')
        price = request.form.get('price_product')
        brand_prod = request.form.get('brand_product')

        add = Product(name=product, price=price, brand=brand_prod)

        # try:
        #     db.session.add(add)
        #     db.session.commit()
        # except Exception:
        #     message = 'Error'

        list_br = []
        all = Brand.query.all()
        for br in all:
            list_br.append(br.name)

        if product and price != '':
            if str(brand_prod) in list_br:
                db.session.add(add)
                db.session.commit()
                #message = 'product was added'
                return redirect('index')
            message = 'brand not exist! create brand!'

    return render_template('index.html', message=message, brand_posts=brand_posts, product_posts=product_posts)


@app.route('/delete_product/<id>')
def delete_product(id):
    dl = db.session.query(Product).get(id)
    db.session.delete(dl)
    db.session.commit()
    return redirect('/index')

@app.route('/delete_brand/<name>')
def delete_brand(name):
    dl_list = Product.query.filter_by(brand=name).all()
    for dl1 in dl_list:
        db.session.query(Product).get(dl1.id)
        db.session.delete(dl1)
        db.session.commit()

    dl = db.session.query(Brand).get(name)
    db.session.delete(dl)
    db.session.commit()
    return redirect('/index')

if __name__ == "__main__":
    app.run()