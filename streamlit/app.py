import streamlit as st
import pandas as pd
import numpy as np

st.write('Sample App')
# "Hello Workd"
# st.write(1234)
# st.markdown("*Streamlit* is **really** ***cool***.")
# st.markdown('''
#     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#     :gray[pretty] :rainbow[colors].''')
# st.markdown("Here's a bouquet &mdash;\
#             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# multi = '''If you end a line with two spaces,
# a soft return is used for the next line.

# Two (or more) newline characters in a row will result in a hard return.
# '''
# st.markdown(multi)
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40],
# }))

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40],
# })

# st.dataframe(df.style.highlight_max(axis=0))

# st.json({
#     'data': {
#         'name': 'test',
#         'age': 20,
#         'info': {
#             'like': 'aaaa'
#         }
#     }
# })

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# st.area_chart(chart_data)
# st.line_chart(chart_data)


# if st.checkbox('click'):
#     st.write('on')

# options = st.multiselect(
#     'What are your favorite colors',
#     ['Green', 'Yellow', 'Red', 'Blue'],
#     ['Yellow', 'Red'])

# st.write('You selected:', options)
# st.write(f'選択肢：{options}')

# size = st.slider('Pick number', 0, 100)

# color = st.select_slider(
#     'Select a color of the rainbow',
#     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
# st.write('My favorite color is', color)

_size = st.sidebar.slider('Pick number', 0, 100)
st.sidebar.write(f'number：{_size}')

left_col, right_col = st.columns(2)
left_col.slider('Pick a Num in Left', 0, 100)
right_col.slider('Right Column')
