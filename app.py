from flask import Flask, jsonify, request
app = Flask("__name__")

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/hithere')
def hi_everyone_there_():
    return "I just hit/hith"

# This handles either GET or POST request
@app.route('/add_two_nums', methods=["POST", "GET"])
def add_two_nums():
    #Get x,y from the posted data
    dataDict = request.get_json()
    x = dataDict["x"]
    y = dataDict["y"]
    

    #Add z=x+y
    z = x+y

    #prepare a json "z":z
    retJSON = {
        "z":z
    }

    #return jsonify(map prepared)
    return jsonify(retJSON), 200



# This is a definitely a GET request
@app.route('/bye')
def bye():
    #Prepare a respose for the request tat came to /bye
    c = 2*534
    s = str(c)

    retJson = {
        'Name':'tola',
        'Age':'22',
        "phones":[

            {
                "phoneName":"Iphone8",
                "phoneNumber": 11111
            },
            {
                "phoneName":"Nokia",
                "phoneNumber": 11111
            }

        ]


    }
    return jsonify(retJson)


# PUT REQUEST
@app.route('/update_me/<id>', methods="PUT")
def update():
    return jsonify({'msg': 'Your id ' +id+ ' has been updated'})

# DELETE REQUEST
@app.route('/delete_me/<id>', methods="DELETE")
def delete():
    return jsonify({'msg': 'Id '+id+' has been deleted'})


if "__name__" == "__main__":
    app.run(debug=True)
