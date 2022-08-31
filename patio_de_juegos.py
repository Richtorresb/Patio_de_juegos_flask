from flask import Flask, render_template

app = Flask(__name__)

#Nivel 1
@app.route('/play')
def play():
    return render_template('index.html')

#Nivel 2
@app.route('/play/<int:num>')
def play_box(num):
    return render_template('index2.html',num=num)

#Nivel 3
@app.route('/play/<int:num>/<string:color>')
def play_color(num,color):
    estilo = f'style=background-color:{color}'
    return render_template('index3.html',num=num,estilo=estilo)

if __name__ =='__main__':
    app.run(debug=True)