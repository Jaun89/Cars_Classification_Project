import streamlit as st
import pandas as pd 

st.title("Cars based on your choice")
st.write("This Machine is used to suggest you Cars based on your choice")

st.sidebar.title("Price")
Price=st.sidebar.slider("Select your price",500000,5000000,500000)

st.sidebar.title("Choose a Color")
Color = st.sidebar.selectbox(
    "Select a color:",
    ("Red", "Black", "Blue", "White", "Grey")
)


st.sidebar.title("Type")
Type = st.sidebar.selectbox("Select Type",
                     ["Comfort" , "Basic uses" , "Show off" , "Speed"]
)


st.sidebar.title("Seats")
Seats = st.sidebar.slider("Choose amount of Seats",2,6,4)

df = pd.read_csv("cars.csv")


# prediction

filtered_cars = [
            (df["Price"] <= Price) &    
            (df["Color"] == Color) &
            (df["Type"] == Type) &
            (df["Seats"] == Seats)
]

st.subheader("Recommended Cars Data set : ")
st.write(df)

filtered_cars = df[
    (df["Price"] <= Price) &
    (df["Color"].str.lower() == Color.lower()) &
    (df["Type"].str.lower() == Type.lower()) &
    (df["Seats"] == Seats)
]

# Show results
st.subheader("Recommended Cars:")
if not filtered_cars.empty:
    st.table(filtered_cars)
else:
    st.warning("No Cars match your criteria. Try adjusting the filters.")


