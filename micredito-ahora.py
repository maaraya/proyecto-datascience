from os import error
from re import A
from numpy.core.numeric import NaN
import streamlit as st
import numpy as np
import pandas as pd
import pickle
from streamlit.proto.Empty_pb2 import Empty
from PIL import Image

st.set_page_config(layout="wide")

image = Image.open('logo.png')

st.sidebar.image(image, use_column_width = True)

def evaluar(valor):
                if valor==1:
                    return 'Puede'
                else:
                    return 'No puede'

def main():
    st.title("Quiero mi crédito ahora!")
    menu = ['Evaluación', 'Test formulario','Acerca de nuestro proyecto' ]
    choice = st.sidebar.selectbox('Menu',menu)

    if choice == 'Evaluación':
        
        st.subheader('Pre-Evaluación Crédito')
        st.text('Realice su pre-evaluación de financiamiento complete los campos solicitados')
        with st.form(key='evaluador'):
            
            col1, col2 = st.beta_columns([1,1])

            with col1:
                
                B015a = st.selectbox('¿Utilizó Bancos como fuente de financiamiento durante el año?',['SI','NO'], help=('Línea de crédito, Crédito de Consumo, Leasing, Factoring, etc.'))

                if B015a == 'SI':
                    varB015 = 1
                else:
                    varB015 = 0
                
                varC064 = st.number_input('Obligaciones con Instituciones financieras Corto Plazo en miles de pesos')
                varC067 = st.number_input('Obligaciones con Instituciones financieras Largo Plazo en miles de pesos')
                varlogC067 = np.log(varC067+1)
                
                                
                B011a = st.selectbox('¿Cuenta con Factoring como producto financiero?', ['SI','NO'])        
               
                if B011a == 'SI':
                    varB011 = 1
                else:
                    varB011 = 0        
                B018a = st.selectbox('¿Utilizó fuentes de financiamiento distintas de bancos como fuente de financiamiento durante el año?',['SI','NO'])        
                
                if B018a == 'SI':
                    varB018 = 1
                else:
                    varB018 = 0               

                varC056 = st.number_input('Gastos Anuales en miles de pesos')
                varlogC056 = np.log(varC056+1)
                varC041 = st.number_input('Total Ingresos Anuales en miles de pesos')

                B099a = st.selectbox('¿Cree que la entidad requerirá créditos en los próximos 12 meses para refinanciamiento?', ['SI','NO'])        
                
                if B099a == 'Si':
                    varB099 = 1
                else:
                    varB099 = 0 

                B090a = st.selectbox('¿La empresa invirtió en adquisición reparación y mantención de Activo Fijo Vehículos y transporte durante el año?', ['SI', 'NO'])        
               
                if B090a == 'SI':
                    varB090 = 1
                else:
                    varB090 = 0 
                
                B098a = st.selectbox('¿Cree que requerirá créditos en los próxmos 12 meses para maquinarias y/o equipos y/o herramientas y/o muebles?', ['SI', 'NO'])        
                
                if B098a == 'SI':
                    varB098 = 1
                else:
                    varB098 = 0 
                
                st.write('\n')
                submit_button = st.form_submit_button(label='Evaluar')


            with col2:            

                B096a = st.selectbox('¿Cree que requerirá crédito en los próximos 12 meses para Capital de trabajo?', ['SI','NO'], help=('Dinero en efectivo en caja o banco, compra materias primas, pago salarios, entre otros'))        
                if B096a == 'SI':
                    varB096 = 1
                else:
                    varB096 = 0

                B012a = st.selectbox('¿Su entidad cuenta con Leasing Operacional y/o financiero, como productos financieros?', ['SI','NO'])  
          
                if B012a == 'SI':
                    varB012 = 1
                else:
                    varB012 = 0
        
                B101a = st.selectbox('¿Cree que NO requerirá crédito en los próximos 12 meses?', ['SI','NO']) 
                if B101a == 'SI':
                    varB101 = 1
                else:
                    varB101 = 0

                B021a = st.selectbox('¿Utilizó Recursos propios o aumentos de capital como financiamiento?',['SI', 'NO']) 
                if B021a == 'SI':
                    varB021 = 1
                else:
                    varB021 = 0

                B095a = st.selectbox('¿No realizó ninguna inversión o adquisición de activos durante el año?', ['SI','NO'])       
                
                if B095a == 'SI':
                    varB095 = 1
                else:
                    varB095 = 0

                B001a = st.selectbox('¿La empresa cuenta con línea de crédito como producto financiero?', ['SI', 'NO'])   

                if B001a == 'SI':
                    varB001 = 1
                else:
                    varB001 = 0
             
                B029a = st.selectbox('¿La empresa no utilizó ningún tipo de financiamientodurante el año?', ['SI','NO'])      
                if B029a == 'SI':
                    varB029 = 1
                else:
                    varB029 = 0 
                
                B002a = st.selectbox('¿La empresa cuenta con tarjeta de crédito bancaria, como productos financieros?', ['SI', 'NO'])     
              
                if B002a == 'SI':
                    varB002 = 1
                else:
                    varB002 = 0
    
                B017a = st.selectbox('¿La empresa utilizó Proveedores como fuente de financiamiento durante el año?', ['SI','NO']) 
                
                if B017a == 'SI':
                    varB017 = 1
                else:
                    varB017 = 0
                B091a = st.selectbox('¿La empresa invirtió en adquisición,reparación y mantención de AF maquinarias herramientas y/o muebles durante el año?', ['SI', 'NO'])        

                if B091a == 'SI':
                    varB091 = 1
                else:
                    varB091 = 0 

            
                

        if submit_button:
            df_temp = pd.DataFrame({'B001':varB001,'B002':varB002,'B011':varB011,'B012':varB012,'B021':varB021,'B029':varB029,
                                    'B090':varB090,'B095':varB095,'B096':varB096,'B099':varB099,'B101':varB101,'log_C056':varlogC056, 'log_C067':varlogC067},
                                     index=(list(range(0,1))))
            #st.dataframe(df_temp)           
            
            #Extraer archivos pickle
            with open('Grupo2_model_vc_credito.sav', 'rb' ) as mo:
                modelo_1 = pickle.load(mo)
            
            #Función aplicar modelo
            
            st.success('Su entidad 'f'{evaluar(modelo_1.predict(df_temp))}' ' acceder a un crédito')

            #st.success('Su entidad puede o no puede acceder a un crédito')



        with st.form(key='Formulario'):
            st.text('Ingrese sus datos y un ejecutivo de nuestros servicios financieros asociados se contactará a la brevedad con usted')
            column1, column2, column3 = st.beta_columns([3,2,1])

            with column1:
                nombreentidad = st.text_input('Nombre Entidad')
                tamanoentidad = st.selectbox('Seleccione Tamaño Entidad',['Grandes Empresas', 'PYME', 'Microempresa'],
                                                 help = ('Seleccione el tamaño de su entidad basado en sus ingresos anuales totales: Grandes empresas: sobre 20.000 UF anuales,  PYME: Ingresos anuales entre x y x,  Micro:  Ingresos anuales entre x y x'))
                telefono = st.text_input('Número de contacto')

                submit_button = st.form_submit_button(label='Ingresar')

            with column2:            
                fe = st.date_input('Fecha Evaluación')
        
        if submit_button:
            st.success('Su evaluación ha sido ingresada con éxito el 'f'{fe}'' gracias!')

    if choice == 'Test formulario':

        df_temp2 = pd.DataFrame({'B001':1,'B002':0,'B011':1,'B012':0,'B021':1,'B029':0,'B090':1,
                                    'B095':1,'B096':0,'B099':0,'B101':1,'log_C056':0,'log_C067':0}, 
                                     index=(list(range(0,1))))

        st.write(df_temp2)


        with st.form(key='columns_in_form'):
            cols = st.beta_columns(len(df_temp2.columns))
            columns = list(df_temp2.columns)
            for i, col in enumerate(cols):
                col.selectbox(columns[i],df_temp2[columns[i]], key=str(i))
            submitted = st.form_submit_button('Submit')

        if submitted:
            
            with open('Grupo2_model_vc_credito.sav', 'rb' ) as mo2:
                modelo_2 = pickle.load(mo2)

            st.success(f'Su entidad {evaluar(modelo_2.predict(df_temp2))} acceder a un crédito')

    if choice == 'Acerca de nuestro proyecto':
        st.write('Quiero mi crédito ahora!!! es una plataforma digital online que permite conectar a empresas en necesidad de crédito con entidades financieras')

        st.write("""<h3>¿Por qué elegir nuestra plataforma?</h3>

* Nuestro plataforma dispone de un sistema de inteligencia artificial que permite evaluar de manera rápida y sencilla si la entidad es sujeta de crédito para la banca privada

* La información de la entidades evaluadas favorablemente se disponibiliza en un pool de evaluaciones donde pueden ser rescatadas por alguna de las entidades financieras asociadas a nuestra plataforma
        
<h3>¿De dónde obtenemos la información?</h3>

* Quinta Encuesta Longitudinal Empresarial (ELE-5)

* Aplicada 2017

* Muestra 6.480 empresas (ventas ≥ UF 800)

* La encuesta está compuesta por 5 módulos. Para construir el modelo solo fue considerado el módulo de Contabilidad y Finanzas, tomando en consideración que solo los atributos financieros de la entidad, que resultan relevantes en la evaluación crediticia.

* Se considera 32 preguntas, de las cuales el modelo utiliza sólo 7, correspondientes a 13 atributos.
        """,unsafe_allow_html=True)            

        image2 = Image.open('2.PNG')
        image3 = Image.open('3.PNG')

        col1, col2 = st.beta_columns([1,1])

        with col1:
            st.image(image2)
        with col2:
            st.image(image3)
        st.write("""
        <h3>¿Cómo predecir la posibilidad de acceso al crédito?</h3>

*Definición del Vector Objetivo.*

Utilizamos como base para construir el VO:

* La entidad obtuvo crédito durante el período

* Crédito fue aprobado, pero no aceptó las condiciones ofrecidas

* Crédito fue aprobado, pero se desiste de tomar el crédito

<h3>¿Cómo determinamos que variables son significativas para el modelo?</h3>""",unsafe_allow_html=True)    

        image4 = Image.open('4.PNG')
        st.image(image4)

if __name__ == '__main__':
    main()
