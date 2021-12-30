import pandas as pd
import streamlit as st
from pycaret.regression import*

# carregando o modelo do disco
model = load_model('extra_trees')

# Título do data app
st.title('Data App - Predição do Preço de Alugueis')

# subtítulo
st.markdown('Este é um Data App para exibir a solução de Machine Learning')

st.sidebar.subheader('Defina os atributos do imóvel para prever o aluguel')

# mapeando dados de entrada do usuário
area = st.sidebar.number_input(label='Área total', value=0, step=1)
num_quartos = st.sidebar.number_input(label='Núm. de quartos', value=0, step=1)
num_banheiros = st.sidebar.number_input(label='Núm. de banheiros', value=0, step=1)
num_andares = st.sidebar.number_input(label='Núm. de Andares', value=0, step=1)
garagem = st.sidebar.number_input(label='Vagas de garagem', value=0, step=1)
mobilia = st.sidebar.selectbox('Imóvel mobiliado?', ('Sim', 'Não'))
#transformando mobilia
mobilia = 1 if mobilia == 'Sim' else 0

valor_condominio = st.sidebar.number_input(label='Valor do condomínio', value=0.00, step=0.01, format="%.2f")
valor_iptu = st.sidebar.number_input(label='Valor do IPTU', value=0.00, step=0.01, format="%.2f")
valor_seguro = st.sidebar.number_input(label='Valor seguro incêndio', value=0.00, step=0.01, format="%.2f")
cidade_sao_paulo = st.sidebar.selectbox('A cidade é São Paulo?', ('Sim', 'Não'))
# formatando cidade
cidade_sao_paulo = 1 if cidade_sao_paulo == 'Sim' else 0

# criando um botão na tela
btn_predict = st.sidebar.button('Iniciar Predição')

if btn_predict:
    df_teste = pd.DataFrame()
    
    df_teste['area'] = [area]
    df_teste['num_quartos'] = [num_quartos]
    df_teste['num_banheiros'] = [num_banheiros]
    df_teste['num_andares'] = [num_andares]
    df_teste['garagem'] = [garagem]
    df_teste['mobilia'] = [mobilia]
    df_teste['valor_condominio'] = [valor_condominio]
    df_teste['valor_iptu'] = [valor_iptu]
    df_teste['valor_seguro_incendio'] = [valor_seguro]
    df_teste['cidade_São Paulo'] = [cidade_sao_paulo]
    
    st.dataframe(df_teste)
    # Realizando a predição
    result = predict_model( model,
                       data = df_teste
                       )["Label"]

    st.subheader('Preço do aluguel previsto: R$ '+str(round(result[0],2)))