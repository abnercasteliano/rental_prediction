from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import pandas as pd

# carregando o modelo do disco
model = pickle.load(open('extra_trees.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    #### POST ####
    if request.method == 'POST':
        #area
        area=request.form['area']

        #num_quartos
        num_quartos=request.form['num_quartos']

        #num_banheiros
        num_banheiros=request.form['num_banheiros']

        #num_andares
        num_andares=request.form['num_andares']

        #garagem
        garagem=request.form['garagem']

        #mobilia
        mobilia=request.form['mobilia']
        if(mobilia=='Sim'):
            mobilia=1
        else:
            mobilia=0

        #valor_condominio
        valor_condominio=request.form['valor_condominio']

        # valor_iptu
        valor_iptu=request.form['valor_iptu']

        # valor_seguro_incendio
        valor_seguro_incendio=request.form['valor_seguro_incendio']

        #cidade_sao_paulo
        cidade_sao_paulo=request.form['cidade_sao_paulo']
        if(cidade_sao_paulo=='Sim'):
            cidade_sao_paulo=1
        else:
            cidade_sao_paulo=0
        
        teste = pd.DataFrame()

        teste['area'] = [area]
        teste['num_quartos'] = [num_quartos]
        teste['num_banheiros'] = [num_banheiros]
        teste['num_andares'] = [num_andares]
        teste['garagem'] = [garagem]
        teste['mobilia'] = [mobilia]
        teste['valor_condominio'] = [valor_condominio]
        teste['valor_iptu'] = [valor_iptu]
        teste['valor_seguro_incendio'] = [valor_seguro_incendio]
        teste['cidade_São Paulo'] = [cidade_sao_paulo]

        prediction = model.predict(teste)

        # Realizando a predição
        result = round(prediction[0],3)

        if result<0:
            return render_template('index.html', prediction_texts="Este imóvel não pode ser vendido")
        else:
            return render_template('index.html', prediction_texts="Preço do aluguel estimado: R$ "+str(result).replace('.',',')+'0')
     
    else:
        return render_template('index.html')
        
if __name__ == "__main__":
    app.run(debug=True)