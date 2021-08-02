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
    menu = ['Evaluación', 'Acerca de nuestro proyecto', 'Test formulario']
    choice = st.sidebar.selectbox('Menu',menu)

    if choice == 'Evaluación':
        
        st.subheader('Pre-Evaluación Crédito')
        st.text('Realice su pre-evaluación de financiamiento complete los campos solicitados')
        with st.form(key='evaluador'):
            
            col1, col2, col3 = st.beta_columns([3,2,1])

            with col1:
                st.text('¿Utilizó Bancos como fuente \n de financiamiento durante el año?')
                
                B015a = st.checkbox('Si utilicé financiamiento', help=('Línea de crédito, Crédito de Consumo, Leasing, Factoring, etc.'))
                B015b = st.checkbox('No utilicé financiamiento')
                if B015a == True:
                    varB015 = 1
                elif B015b == True:
                    varB015 = 0
                
                varC064 = st.number_input('Obligaciones con Instituciones financieras Corto Plazo en miles de pesos')
                varC067 = st.number_input('Obligaciones con Instituciones financieras Largo Plazo en miles de pesos')
                                
                st.text('¿Cuenta con Factoring \ncomo producto\nfinanciero')
                B011a = st.checkbox('No Cuento con Factoring')        
                B011b = st.checkbox('Cuento con Factoring')
                if B011a == True:
                    varB011 = 1
                elif B011b == True:
                    varB011 = 0        

                st.text('¿Utilizó fuentes de financiamiento \ndistintas de bancos como fuente\nde financiamiento durante el año')
                B018a = st.checkbox('No cuento con fuentes de financiamiento distintas a Bancos')        
                B018b = st.checkbox('Si cuento con fuentes de financiamiento distintas a Bancos')
                if B018a == True:
                    varB018 = 1
                elif B018b == True:
                    varB018 = 0               

                varC056 = st.number_input('Gastos Anuales en miles de pesos')
                varlogC056 = np.log(varC056+1)
                varC041 = st.number_input('Total Ingresos Anuales en miles de pesos')

                st.text('¿Cree que la entidad requerirá \ncréditos en los próximos 12\nmeses para refinanciamiento')
                B099a = st.checkbox('No requerirá crédito para refinanciamiento')        
                B099b = st.checkbox('Si requerirá crédito para refinanciamiento')
                if B099a == True:
                    varB099 = 1
                elif B099b == True:
                    varB099 = 0 

                st.text('¿La empresa invirtió en adquisición\nreparación y mantención de\nActivo Fijo Vehículos y transporte\n durante el año')
                B090a = st.checkbox('No invirtió en adquisición, mantención o reparación de AF')        
                B090b = st.checkbox('Si invirtió en adquisición, mantención o reparación de AF')
                if B090a == True:
                    varB090 = 1
                elif B090b == True:
                    varB090 = 0 
                
                st.text('¿Cree que requerirá créditos\nen los próxmos 12 meses para\nmaquinarias y/o equipos y/o \nherramientas y/o muebles')
                B098a = st.checkbox('Si requerirá créditos')        
                B098b = st.checkbox('No requerirá créditos')
                if B098a == True:
                    varB098 = 1
                elif B098b == True:
                    varB098 = 0 

                st.text('¿La empresa invirtió en adquisición,\nreparación y mantención de\nAF maquinarias herramientas y/o muebles\n durante el año?')
                B091a = st.checkbox('Si invirtió en adquisición o reparación')        
                B091b = st.checkbox('No invirtió en adquisición o reparación')
                if B091a == True:
                    varB091 = 1
                elif B091b == True:
                    varB091 = 0 




            with col2:            
                st.text('¿Cree que requerirá \ncrédito en los próximos\n12 meses para Capital de \ntrabajo?')
                B096a = st.checkbox('Si requeriré crédito para capital de trabajo', help=('Dinero en efectivo en caja o banco, compra materias primas, pago salarios, entre otros'))        
                B096b = st.checkbox('No requeriré crédito para capital de trabajo')
                if B096a == True:
                    varB096 = 1
                elif B096b == True:
                    varB096 = 0
                
                st.text('¿Su entidad cuenta \ncon Leasing Operacional\ny/o financiero, como \nproductos financieros?')
                B012a = st.checkbox('No cuento con estos productos')        
                B012b = st.checkbox('Cuento con estos productos')
                if B012a == True:
                    varB012 = 1
                elif B012b == True:
                    varB012 = 0

                st.text('¿Cree que NO requerirá \ncrédito en los próximos\n12 meses')
                B101a = st.checkbox('No requeriré crédito')        
                B101b = st.checkbox('Si requeriré crédito')
                if B101a == True:
                    varB101 = 1
                elif B101b == True:
                    varB101 = 0

                st.text('¿Utilizó Recursos propios\no aumentos de capital\ncomo financiamiento?')
                B021a = st.checkbox('Si utilicé recursos propios')        
                B021b = st.checkbox('No utilicé recursos propios')
                if B021a == True:
                    varB021 = 1
                elif B021b == True:
                    varB021 = 0

                st.text('¿No realizó ninguna \ninversión o adquisición\nde activos durante el año?')
                B095a = st.checkbox('No realicé inversión o adquisición de activos')        
                B095b = st.checkbox('Si realicé inversión o adquisición de activos')
                if B095a == True:
                    varB095 = 1
                elif B095b == True:
                    varB095 = 0


                st.text('¿La empresa cuenta \ncon línea de crédito\ncomo producto financiero?')
                B001a = st.checkbox('Si cuento con línea de crédito')        
                B001b = st.checkbox('No cuento con línea de crédito')
                if B001a == True:
                    varB001 = 1
                elif B001b == True:
                    varB001 = 0


                st.text('¿La empresa no utilizó \nningún tipo de \nfinanciamientodurante el\naño?')
                B029a = st.checkbox('No utilizó financiamiento de ningún tipo')        
                B029b = st.checkbox('Si utilizó financiamiento')
                if B029a == True:
                    varB029 = 1
                elif B029b == True:
                    varB029 = 0 

                st.text('¿La empresa cuenta con\ntarjeta de crédito\nbancaria, como\nproductos financieros?')
                B002a = st.checkbox('Si cuenta con tarjeta de crédito')        
                B002b = st.checkbox('No cuenta con tarjeta de crédito')
                if B002a == True:
                    varB002 = 1
                elif B002b == True:
                    varB002 = 0
                
                st.text('¿La empresa utilizó\nProveedores como fuente\nde financiamiento\ndurante el año?')
                B017a = st.checkbox('Si utilizó Proveedores como fuente de financiamiento')        
                B017b = st.checkbox('No utilizó Proveedores como fuente de financiamiento')
                if B017a == True:
                    varB017 = 1
                elif B017b == True:
                    varB017 = 0


            with col3:
                submit_button = st.form_submit_button(label='Evaluar')

        if submit_button:
            df_temp = pd.DataFrame({'B001':varB001,'B002':varB002,'B011':varB011,'B012':varB012,'B018':varB018,'B021':varB021,'B029':varB029,
                                    'B090':varB090,'B095':varB095,'B096':varB096,'B098':varB098,'B099':varB099,'B101':varB101,'log_C056':varlogC056},
                                     index=(list(range(0,1))))
            #st.dataframe(df_temp)           
            
            #Extraer archivos pickle
            with open('Grupo2_model_vc_credito.sav', 'rb' ) as mo:
                modelo_1 = pickle.load(mo)
            
            #Función aplicar modelo
            
            st.success('Su entidad 'f'{evaluar(modelo_1.predict(df_temp))}' ' acceder a un crédito')

            #st.success('Su entidad puede o no puede acceder a un crédito')



        with st.form(key='Formulario'):
            st.text('Ingrese sus datos y un ejecutivo de nuestros servicios financieros asociados \nse contactará a la brevedad con usted')
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

        df_temp2 = pd.DataFrame({'B001':1,'B002':0,'B011':1,'B012':0,'B018':1,'B021':0,'B029':1,
                                    'B090':0,'B095':1,'B096':0,'B098':1,'B099':0,'B101':1,'log_C056':0},
                                     index=(list(range(0,1))))

        st.write(df_temp2)


        with st.form(key='columns_in_form'):
            cols = st.beta_columns(14)
            columns = list(df_temp2.columns)
            for i, col in enumerate(cols):
                col.selectbox(columns[i],df_temp2[columns[i]], key=str(i))
            submitted = st.form_submit_button('Submit')

        if submitted:
            
            with open('Grupo2_model_vc_credito.sav', 'rb' ) as mo2:
                modelo_2 = pickle.load(mo2)

            st.success(f'Su entidad {evaluar(modelo_2.predict(df_temp2))} acceder a un crédito')

                    
            


if __name__ == '__main__':
    main()
