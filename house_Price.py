import streamlit as st
import pickle
from streamlit_option_menu import option_menu
#loading the saved model
House_Price = pickle.load(open('House_Price (1).sav','rb'))
#sidebar for navigate

with st.sidebar:
    selected = option_menu("Price Prediction System",

                           ['House Price Prediction',
                            'RealEstate Price Prediction'],

                           icons = ['house-door-fill','phone-landscape'],default_index = 0)

#house_price page
if (selected =='House Price Prediction'):
    #page title
    st.title('House Price Prediction using ML')


    area= st.text_input('Area Required')
    bedrooms=st.text_input('Number of Bedrooms')
    bathrooms=st.text_input('Number of Bathrooms')
    stories=st.text_input('No.of Stories ')
    mainroad=st.text_input('Mainroad Attachment(1/0)')
    guestroom=st.text_input('Guestroom Requirement(1/0)')
    basement=st.text_input('Basement Requirement(1/0)')
    hotwaterheating=st.text_input('Hot Water Requirement(1/0)')
    airconditioning=st.text_input('Air Conditioning Requirement(1/0)')
    parking=st.text_input('Parking Places Required')
    prefarea=st.text_input('Preference Area(1/0)')
    unfurnished=st.text_input('Unfurnishment(1/0)')


    #code for prediction

    price_prediction = ''

    if st.button('Predict Price'):
        house_prediction = House_Price.predict([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement,
                                                 hotwaterheating, airconditioning, parking, prefarea, unfurnished]])
        price_prediction = house_prediction[0]  # Assuming house_prediction is a single value

    if price_prediction:
        st.success(f"The predicted price is: {price_prediction}")




if (selected == "RealEstate Price Prediction"):
    st.title('RealEstate Price Prediction using ML')