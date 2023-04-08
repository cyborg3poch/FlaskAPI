from flask import Flask, request, jsonify

# Creating an instance of Flask class and passing main module ref
app = Flask(__name__)


# using routing decorators
@app.route("/")
def index():
    return "hello World"


@app.route("/<name>")
def print_name(name):
    # not a formatted string using placeholder for format(name)
    return "hello , {}".format(name)


book_list = [
    {"id": 1,
     "name": "harry Potter",
     "author": "JK Rowling"
     },
    {"id": 2,
     "name": "Game of thrones",
     "author": "RR Martin"
     }
]


@app.route("/books", methods=['GET', 'POST'])
def get_books():
    if request.method == 'GET':
        if len(book_list) > 0:
            return book_list
        else:
            return 'NOT Found', 404

    if request.method == 'POST':
        new_title = request.form['name']
        new_author = request.form['author']
        new_id = len(book_list) + 1

        book_obj = {
            "id": new_id,
            "name": new_title,
            "author": new_author
        }

        book_list.append(book_obj)
        return jsonify(book_list), 201


@app.route("/book/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == "GET":
        for book in book_list:
            print(f"Id is{id}")
            print(book["id"])
            if book["id"] == id:
                return jsonify(book)

    if request.method == "PUT":
        new_title = request.form['name']
        new_author = request.form['author']

        for book in book_list:
            if book["id"] == id:
                book["name"] = new_title
                book["author"] = new_author
                return jsonify(book), 200
            
    if request.method == "DELETE":
        for indx, book in enumerate(book_list):
            if book["id"] == id:
                book_list.pop(indx)
                return book_list, 204


# better way is to run "SET FLASK_APP = app.py" and then "flask run"
if __name__ == "__main__":
    app.run(debug=True)
