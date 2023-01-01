from flask import Flask,request,jsonify

app = Flask(__name__)
@app.route('/test_route',methods = ['POST'])
def math_operations_via_flask():
    if(request.method =='POST'):
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if(operation == 'add'):
            r = num1+num2
            result = 'the sum of '+str(num1) + " and " + str(num2)+"is "+str(r)
        if (operation == 'sub'):
            r = num1 - num2
            result = 'the sub of ' + str(num1) + " and " + str(num2) + "is " + str(r)

        if (operation == 'mul'):
            r = num1 * num2
            result = 'the mul of ' + str(num1) + " and " + str(num2) + "is " + str(r)
        if (operation == 'div'):
            r = num1 / num2
            result = 'the div of ' + str(num1) + " and " + str(num2) + "is " + str(r)
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug = True)