from flask import Flask, request, jsonify, render_template;


app = Flask(__name__);

@app.route('/',methods=["GET"])
def index():
    print("index.html page got called")
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def math_operation_via_postman():

    if(request.method=='POST'):
        operation = request.form['operation'] # request.json for postman
        num1=int(request.form['num1']);
        num2=int(request.form['num2']);
        r=0;

        if(operation=='addition'):
            r=num1+num2
        if (operation == 'subtract'):
            r = num1 - num2
        if (operation == 'multiply'):
            r = num1 * num2
        if (operation == 'divide'):
            r = num1 // num2

        print("sum of numbers"+str(num1)+" "+str(num2)+" = " +str(r))

        return render_template("index.html", result=r);

if __name__ =='__main__':
    print("The app is working")
    app.run();



