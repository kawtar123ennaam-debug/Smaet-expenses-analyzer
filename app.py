
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

st.markdown("""
             <style>
            .stApp{
                background-image: url ("backgroubd.jpg");
            }
</style>
""",unsafe_allow_html=True)

st.title("Expenses analysis")


#انشاء قائمة لحفظ

if'data'not in st.session_state:
     st.session_state.data=[]

#الفورم
with st.form("expense_form"):
      data = st.date_input("data")
      category = st.selectbox("category",["food","transport","shopping","travel"])
      amount =st.number_input("amount",min_value=0)

      submitted = st.form_submit_button("+ plus")   
#عند الطغظ على الزر
      if submitted:
           st.session_state.data.append({
                
                "data":data,
                "category" : category,
                "amount": amount

           })
# لدى تواجد بيانات          
if st.session_state.data:
   df =pd.DataFrame(st.session_state.data)

   st.write("All expenses")
   st.dataframe(df)
   by_category = df.groupby("category")["amount"].sum()
   st.write('Expenses by Category')
   st.bar_chart (by_category)
   total=df["amount"].sum()
   st.write("Total expenses",total)

#اكبر و اقل قيمة fig,ax = plt.subplots()
   fig, ax = plt.subplots()    
   by_category.plot(kind="bar",ax=ax)
   st.pyplot(fig)

   max_category = by_category.idxmax()
   min_category = by_category.idxmin()

   st.write("Higher spending:",max_category)
   st.write("lower spending:",min_category)

   st.write(f"Recommendation:Try to reduce spending on {max_category}")

#زر حدف البيانا
   if st.button("Delete data"):
          st.session_state.data =[]

