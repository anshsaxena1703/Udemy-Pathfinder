import streamlit as st
import pickle
import pandas as pd
course_dict = pickle.load(open('courses_dict.pkl','rb'))
courses = pd.DataFrame(course_dict)
st.title('Udemy-Pathfinder')

similarity = pickle.load(open('similarity.pkl','rb'))

data1 = pickle.load(open('data1.pkl','rb'))
def recommend(course):
    course_index = courses[courses['course_name'] == course].index[0]
    distances = similarity[course_index]
    course_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_courses = []
    recommended_courses_images = []
    for i in course_list:
        recommended_courses.append(courses.iloc[i[0]].course_name)
        link = data1.loc[data1['ind'] == i[0]-1, 'course image'].values[0]
        recommended_courses_images.append(link)
    return recommended_courses,recommended_courses_images

selected_course_name = st.selectbox(
    'Select Course',
    courses['course_name'].values)

if st.button('Suggest'):
    names,images = recommend(selected_course_name)

    for name, image in zip(names, images):
        st.header(name)
        st.image(image)
