# Udemy-Pathfinder - [Demo Video](https://drive.google.com/file/d/13QpWdA77LHyvy5g1d_7CG9D1m8XB5Fvp/view?usp=drive_link)
## Project Description
Udemy Pathfinder is a machine learning-powered course recommendation system designed to assist users in discovering the best Udemy courses tailored to their interests. The project involves the following key steps:

**Data Collection:** The dataset was sourced from Kaggle, containing comprehensive details about various 5000 Udemy courses.

**Data Preprocessing:** Important attributes such as course name, overview, and instructor were combined into a tag column to create a rich text representation for each course.

**Vectorization:** The tag column was converted into numerical vectors using CountVectorizer from sklearn.feature_extraction.text. This process transforms textual data into a matrix of token counts, facilitating similarity calculations.

**Similarity Calculation:** Cosine similarity was used to measure the similarity between courses based on the vectorized tag column.

**Web Application:** The project is deployed as an interactive web application using Streamlit, enabling users to select a course and view the top 5 recommended courses along with their images and titles.

## Features
**Course Selection:** Users can browse through a dropdown menu to select a course they are interested in.

**Top 5 Recommendations:** Once a course is selected, the system displays the top 5 similar courses, complete with their titles and images.

**Interactive Web App:** The application is built using Streamlit, providing an easy-to-use interface for real-time course recommendations.

## Usage
### **Step 1: Download the Project Files**

&nbsp;&nbsp;&nbsp; **1. Clone the GitHub Repository:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &bull; Open your terminal or command prompt.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &bull; Change to your desired directory where you want to clone the project.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &bull; Execute the following command to clone the repository: 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `git clone https://github.com/anshsaxena1703/udemy-pathfinder.git`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &bull; Navigate into the cloned project directory: `cd udemy-pathfinder`

### **Step 2: Download the `similarity.pkl` File**

&nbsp;&nbsp;&nbsp; **2. Download the `similarity.pkl` File:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &bull; Access the Google Drive link to download the `similarity.pkl` file: `https://shorturl.at/nOmYC`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &bull; After downloading, move the `similarity.pkl` file into the project directory (`udemy-pathfinder`).

### **Step 3: Install Dependencies and Run the Web App**

&nbsp;&nbsp;&nbsp; **3. Install Dependencies:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &bull; Ensure you are in the project directory (`udemy-pathfinder`).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &bull; Install Streamlit using the following command: `pip install streamlit`

&nbsp;&nbsp;&nbsp; **4. Run the Web Application:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &bull; Start the Streamlit application by executing: `streamlit run app.py`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &bull; Open your web browser and navigate to `http://localhost:8501` to interact with the Udemy Pathfinder.

By following these steps, you can easily set up and run the Udemy Pathfinder, exploring and discovering new courses that match your interests.

