import streamlit as st
import stripe

stripe.api_key="sk_test_4eC39HqLyjWDarjtT1zdp7dc"

st.markdown(""" <style> .main { background-color: #e6ffe6; } .sidebar .sidebar-content { background-color: #ccffcc; } .stButton>button { background-color: #ff69b4; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 8px; } .stButton>button:hover { background-color: #ff1493; } </style> """, unsafe_allow_html=True)


# App title
st.title("Zach Temmy Investments")

# Contact Information
st.sidebar.title("Our Contacts")
st.sidebar.write("Phone: +234 8106757383")
st.sidebar.write("Email: Zachytemmy@gmail.com")
st.sidebar.write("Address: 12 Dalimore Street(opposite Bank of Industry), Ado-Ekiti, Nigeria")

# Order Form
st.header("Place Your Order")
name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
address = st.text_area("Delivery Address")
perfume = st.selectbox("Select Perfume", ["Latafa", "Oud", "Body Spray"])
quantity = st.number_input("Quantity", min_value=1, max_value=10, step=1)
payment_method = st.selectbox("Payment Method", ["Credit Card", "Debit Card", "PayPal"])

if st.button("Submit Order"):
    st.success("Order placed successfully!")


st.header("Payment")
if st.button("Proceed to Payment"):
    try:
        session = stripe.checkout.Session.create( 
            payment_method_types=['card'], 
            line_items=[{ 
                'price_data': { 
                    'currency': 'ngn', 
                    'product_data': { 
                        'name': 'Latafa', 
                    }, 
                    'unit_amount':20000 * 100, 
                }, 
                'quantity': quantity, 
          }],
          mode='payment',
          success_url='https://your-success-url.com', 
          cancel_url='https://your-cancel-url.com', 
        ) 
        st.write(f"Please complete your payment [here]({session.url})") 
    except Exception as e: 
        st.error(f"An error occurred: {e}")


# FAQs
st.header("Frequently Asked Questions")
faq1 = st.expander("What is the delivery time?")
faq1.write("Delivery time is 3-5 business days within Nigeria.")
faq2 = st.expander("What payment methods are accepted?")
faq2.write("We accept Credit Card, Debit Card, and PayPal.")
faq3 = st.expander("Can I return a product?")
faq3.write("Yes, you can return a product within 30 days of purchase.")