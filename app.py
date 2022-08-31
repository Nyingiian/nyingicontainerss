from PIL import Image
import requests 
import streamlit as st
from streamlit_lottie import st_lottie


img_icon = Image.open("/home/nyingi/Desktop/webapp/images/container_icon.jpg")

st.set_page_config(page_title="Nyingi Containers",page_icon=img_icon,layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None 

    return r.json()


#Use Local CSS

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("/home/nyingi/Desktop/webapp/style/style.css")       
#---LOAD ASSETS-----

lottie_coding = load_lottieurl ("https://assets7.lottiefiles.com/packages/lf20_pnjqarcr.json")
img_contact_form = Image.open("/home/nyingi/Desktop/webapp/images/Office.jpg")
img_lottie_animation = Image.open("/home/nyingi/Desktop/webapp/images/shop.jpeg")
img_contact_cafeteria = Image.open("/home/nyingi/Desktop/webapp/images/cafeteria.jpeg")
img_contact_logistics = Image.open("/home/nyingi/Desktop/webapp/images/logistics.jpg")
img_contact_accomodation = Image.open("/home/nyingi/Desktop/webapp/images/accomodation.jpg")
img_contact_Refrigirated = Image.open("/home/nyingi/Desktop/webapp/images/Refrigirated.jpg")
#-------HEADER SECTION -------

with st.container(): 

    st.subheader("Hi, I am Ian Nyingi :wave:")
    st.title("Sales Manager at Cointainer Investment Kenya")
    st.write("We are a world-class shipping container suppliers. We offer the highest quality customized shipping containers for any application")
    st.write("[Learn More>](https://containerinvestmentkenya.co.ke/)")

#-------WHAT WE OFFER------

with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I ensure that our in-house design and engineering team meticulously plans 
            every detail of your project with 3D renderings to capture 
            all of your needs and desires while adhering to all required standards.
        
        """)

    with right_column:
        st_lottie(lottie_coding,height=300, key="coding")

#----PROJECTS------

with st.container():
    st.write("---")
    st.header("Our projects")
    st.write("##")
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:    
        st.subheader("Converting dry shipping containers into stalls")
        st.write(
            """
            We offer upto standard fabrication services that exceeds our customer specifications.
            The structures are used for commercial services and also as storage facilities
            """)
        st.write("[Learn More>]https://containerinvestmentkenya.co.ke/service/dry-containers/")


with st.container():
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:    
        st.subheader("Converting dry shipping containers into offices")
        st.write(
            """
            Our elegant yet functional turnkey portable office unit solutions are ideal for working from home or in any remote location.
            The offices offices are fully insulated, padding with gypsum,electrical wiring, ceramic tiles on the floor and spray painted to color of choice.
            any other customization is also allowed.
            """)
        st.write("[Learn More>]https://containerinvestmentkenya.co.ke/service/container-offices/")

#---------CAFETERIA----------
with st.container():
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(img_contact_cafeteria)
    with text_column:    
        st.subheader("Converting dry shipping containers into Elegant Cafeterias")
        st.write(
            """
            With our modern cafeteria units, you can add a small kitchenette and an optional washroom.
            The structures provides a vibrant and modern space that can be used either temporarily or permanently.
            The results are just amazing. Infact, your imagination is the only limit.
            """)
        st.write("[Learn More>]https://containerinvestmentkenya.co.ke/")


#-----------CONTAINER ACCOMODATION/HOMES--------

with st.container():
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(img_contact_accomodation)
    with text_column:    
        st.subheader("Container Accomodation")
        st.write(
            """
            Our in-house design and engineering team meticulously plans
             every detail of your project with 3D renderings to capture
              all of your needs and desires while adhering to all required standards.
            """)
        st.write("[Learn More>]https://containerinvestmentkenya.co.ke/service/container-accommodation-homes/")


#--------REFRIGIRATED---------------------

with st.container():
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(img_contact_Refrigirated)
    with text_column:    
        st.subheader("Refrigirated Containers")
        st.write(
            """
            In working condition.
            Temperature ranges of between -30 to +30 degrees Celsius.
            A One-year warranty is also offered.
            """)
        st.write("[Learn More>]https://containerinvestmentkenya.co.ke/service/refrigerated-container/")

#------------LOGISTICS---------------

with st.container():
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(img_contact_logistics)
    with text_column:    
        st.subheader("Countrywide Logistics")
        st.write(
            """
            We deliver shipping containers countrywide.
            We are simply a one shop stop for all your container needs.
            """)
        st.write("[Learn More>]https://containerinvestmentkenya.co.ke/service/logistics/")



#-----CONTACT--------
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")


    contact_form = """
    <form action="https://formsubmit.co/nyingicontainers@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value = "false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholer="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form> 
    """

    left_column,right_column= st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)

    with right_column:
        st.empty()