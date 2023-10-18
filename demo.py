import streamlit as st
import pandas as pd

#remove header at the top of the page and footer at the bottom
#(by inspecting html. copy classes to hide and specify with dots: .classname, 
# removing possible spaces)
st.markdown("""
<style>
.st-emotion-cache-18ni7ap.ezrtsby2
{
            visibility: hidden;
}     
</style>""", unsafe_allow_html=True)
st.markdown("""
<style>
.st-emotion-cache-h5rgaw.ea3mdgi1
{
            visibility: hidden;
}     
</style>""", unsafe_allow_html=True)

st.markdown("""
<style>
.viewerBadge_link__qRIco
{
            visibility: hidden;
}     
</style>""", unsafe_allow_html=True)

st.title("Hi! I am Streamlit Web App 2")
st.subheader("Hi! I am your Subheader")
st.header("I am Header")
st.text("Hi I am text function and programmers use me inplace of paragraph tag")
st.markdown("**Hello** *World*!")
st.markdown("# Hello World!")
st.markdown("---")
st.markdown("[Markdown Guide](https://www.markdownguide.org/cheat-sheet/)")
st.markdown("---")
st.caption("Hi, I am caption")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

json={"a":"1,2,3","b":"4,5,6"}
st.json(json)

code="""
print("Hello World")
def funct()
    reurn 0;
"""
st.code(code, language="python")

st.write("## H2")

st.metric(label="Wind Speed", value="120ms⁻¹",delta="1.4ms⁻¹")
st.metric(label="Wind Speed", value="120ms⁻¹",delta="-1.4ms⁻¹")

table=pd.DataFrame({"Column 1": [1,2,3,4,5,6,7],"Column 2": [11,12,13,14,15,16,17]})
st.table(table) #static
st.dataframe(table) #interactive

st.image("image.jpg",caption="This is my Image",width=680)
st.audio("audio.wav")
st.video("video.mp4")

state=st.checkbox("Checkbox 1",value=True)
if state:
    st.write("Hi")
else:
    pass


def change():
    print("Changed") #on terminal
state=st.checkbox("Checkbox 2",value=True, on_change=change)


def check():
    print(st.session_state.checker) #on terminal
state=st.checkbox("Checkbox 3",value=True, on_change=check,key="checker")

radio_btn=st.radio("In which Country do you live?",options=("US","UK","Canada"))
print(radio_btn)

def btn_click():
    print("Button clicked!")
btn=st.button("Click Me!",on_click=btn_click)

select=st.selectbox("What is your favourite car?",options=("Audi","BMW","Ferrari"))
print(select)

multiple_select=st.multiselect("What is your favourite Tech Brand?",options=("Apple","Samsung","Xiaomi","Sony"))
st.write(multiple_select)
