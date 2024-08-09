import streamlit as st

st.code("import pandas as pd")
julia_code="""
function doit(num::int)
	println(num)
end
"""
st.code(julia_code,language='julia')
if st.button("Balloons"):
	st.balloons()
