# -*- coding: utf-8 -*-
"""Lesson 94 - 13-6-2023

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13-8nYq0UAl9S33gicnbIQYTUl6P1R8R-

# Lesson 94 -  Streamlit Widgets I

### Teacher-Student Activities

In the previous class, we built a machine learning web app capable of predicting species of Iris flower using Streamlit. We also explored few Streamlit widgets like sliders and select box that makes our application more interactive. Today, we will learn more such Streamlit widgets by implementing a multiclass classification model in the form of a web app. Before that, we will learn how to host web apps using Streamlit sharing.

Let's quickly go through the activities covered in the previous class and begin this class from **Activity 1: Hosting using Streamlit Sharing** section.

---

#### Activity 1: Hosting Using Streamlit 'Sharing'

Now that you've created your app, you're ready to share it! We have already used Heroku server to host our Streamlit app. Let us explore  an even more easier way of hosting your web apps using the **Streamlit Sharing** service. Just quickly skim through its website (https://streamlit.io/sharing) to get yourself acquainted with it.

In one of the previous classes, we had requested an invite from Streamlit community by visiting the [Streamlit sharing link](https://streamlit.io/sharing-sign-up) and filled-up the following sign-up form:

<center><img src="https://i.imgur.com/ivcXEmq.png" width=600></center>

By now, you may have received an invite email like this:

<center><img src="https://s3-whjr-v2-prod-bucket.whjr.online/3200fc8c-5d47-4304-938e-79e799e6c685.PNG"></center>

Now you're ready to deploy your Streamlit apps using Streamlit 'Sharing' service. You'll need a GitHub account that uses the same email id of your's as your Streamlit account.

**Note:** In case, you have still not created a GitHub account, refer to the video provided below until the **timestamp 2:57**.

https://www.youtube.com/watch?v=EO8o6avuULE

**Step 1: Push your app on GitHub**

- To get started, log into [GitHub](https://github.com/) account and create a new repository. Name your repository as `"improved-iris-streamlit-sharing"` or you may provide any name of your choice.

  Make sure that your repository is **Public** as Streamlit Sharing only hosts public GitHub repositories.

  <center><img src="https://s3-whjr-v2-prod-bucket.whjr.online/dbbb5064-f0b5-47e1-b39a-77d13b3bc8ca.PNG"></center>

- Upload the following three files on your public GitHub repository:
    - **improved_iris_app.py:** This is the Python file containing the Iris flower species classification that you had created in the previous activities.
    - **requirements.txt:** This file specifies which Python packages are required to run the project. We need not learn more about this file as it is beyond the scope of this course.
    - **iris-species.csv:** This is our dataset file.

  You can download these files from the link given below:

  https://drive.google.com/drive/folders/1fxfzQaGKW7k3-RVq4iS1vVBiA6pZKYA2

**Step 2: Sign in into Streamlit Sharing**

  - Visit https://share.streamlit.io/ and sign in with a Github account that Streamlit Sharing has granted access to use it.

  - After sign-in, click on the **New app** button.

  <center><img src="https://s3-whjr-v2-prod-bucket.whjr.online/78206c92-1487-42dc-b420-839f6b55d87c.PNG"></center>


**Step 3: Deploy your app**

  - Select the values of the required fields on the Deploy page. When you will click on the first field, it will give you auto-suggestion of all the public repositories hosted on your Github account. You need to select the one which you created in **Step 1** (`"improved-iris-streamlit-sharing"`) and then pass the name of your branch you want to deploy.

  - Pass the name of the Branch (in our case, it is **main**) and file path (name of your `.py` file). You will get auto-suggestions for branch name and file path once you have chosen your desired repository.

**Note:** Sometimes auto-suggestion does not work for the third field i.e. `Main file path` . In that case, you may need to manually enter the name of your python (`.py`) file uploaded on the GitHub repository.
  <center><img src="https://s3-whjr-v2-prod-bucket.whjr.online/8f5d57c4-21cf-4038-aaed-acc6f1ad2c00.PNG"></center>

That's it—you're done! Your app can be found at:

```
https://share.streamlit.io/[user name]/[repo name]/[branch name]/[app path]
```

For Example:

https://share.streamlit.io/whitehatjr-test/improved-iris-streamlit-sharing/main/improved_iris_app.py


As with all hosted Streamlit apps, you can continuously update your app by editing the `.py file` on GitHub.

**Notes:**

  1. It may take about 15 to 20 minutes for the deployment of your streamlit webapp.

  2. You can also refer to the video link given below to understand the complete process of hosting Streamlit apps using the Streamlit Sharing service.

 https://youtu.be/bjt6bpoNM4I

---

#### Problem statement

Recall the glass-type classification that you had performed in one of your previous classes wherein you classified different types of glasses based on their chemical and physical composition.

**Dataset Description:**

The dataset used in this problem statement involves the classification of samples of different glasses based on their physical and chemical properties. They are as follows:

1. **RI:** Refractive Index

2. **Na:** Sodium

3. **Mg:** Magnesium

4. **Al:** Aluminum

5. **Si:** Silicon

6. **K:** Potassium

7. **Ca:** Calcium

8. **Ba:** Barium

9. **Fe:** Iron

There are seven types (classes or labels) of glass listed; they are:

* **Class 1:** used for making building windows (float processed)

* **Class 2:** used for making building windows (non-float processed)

* **Class 3:** used for making vehicle windows (float processed)

* **Class 4:** used for making vehicle windows (non-float processed)

* **Class 5:** used for making containers

* **Class 6:** used for making tableware

* **Class 7:** used for making headlamps

**Dataset Credits:** https://archive.ics.uci.edu/ml/datasets/Glass+Identification

**Citation:** Dua, D., & Graff, C.. (2017). UCI Machine Learning Repository

---

#### Activity 2: Importing Modules and Loading Data

First create a Python file `glass_type_app.py` in Sublime editor and save it in `Python_scripts` folder created earlier. Copy the code given below in `glass_type_app.py` file.

The code given below performs the following tasks: *(learnt in **Logistic Regression - Multiclass Classification I**)*

1. Imports the necessary Python modules including `streamlit`.

2. Drops the unnecessary columns and provides suitable column headers to the independent variables.

3. Creates feature and target variables.

4. Splits the dataset into train and test sets using the `train_test_split()` function.

**Note:** Do not run the code shown below. It will thrown an error.
"""

# S2.1: Open Sublime text editor, create a new Python file, copy the following code in it and save it as 'glass_type_app.py'.
# You have already created this ML model in ones of the previous classes.

# Importing the necessary Python modules.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.model_selection import train_test_split


# Loading the dataset.
@st.cache()
def load_data():
    file_path = "glass-types.csv"
    df = pd.read_csv(file_path, header = None)
    # Dropping the 0th column as it contains only the serial numbers.
    df.drop(columns = 0, inplace = True)
    column_headers = ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'GlassType']
    columns_dict = {}
    # Renaming columns with suitable column headers.
    for i in df.columns:
        columns_dict[i] = column_headers[i - 1]
        # Rename the columns.
        df.rename(columns_dict, axis = 1, inplace = True)
    return df

glass_df = load_data()

# Creating the features data-frame holding all the columns except the last column.
X = glass_df.iloc[:,:-1]

# Creating the target series that holds last column.
y = glass_df['GlassType']

# Spliting the data into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(X , y , test_size = 0.30 , random_state = 42 )

"""**Note:** You have to store the `glass-types.csv` file in your computer in the same folder that contains the above Python script. You can download the `glass-types.csv` file from the link provided below.

https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/glass-types.csv

In the above code, we encapsulated some part of the code inside a function `load_data()` and added `st.cache()` decorator at the start of this function. Let us understand why?

**The `st.cache()` decorator:**

- Each time when you rerun your Streamlit app or change any widget value, the whole app runs from start to end.
- This is not feasible when we create complicated machine learning apps as it will consume lot of time in rerunning the entire app.
- Streamlit provides a functionality called **caching**, where data is not loaded each time when the app is loaded. Instead the data is loaded from the local cache (a temporary storage location on your machine). This saves cpu cycles and memory time, thereby improving the performance of your web app.


In our case, we added `@st.cache()` decorator at the start of `load_data()` function as this part of code will not change more often.

---

#### Activity 3: Adding `prediction()` Function

As done in the previous class, let us add a function, say `prediction()`, that will predict the type of glass for every unique combination of `RI`, `Na`, `Mg`, `Al`, `Si`, `K`, `Ca`, `Ba` and `Fe` values. Follow the steps given below to create this function:

1. The `prediction()` function takes 2 inputs:

  - `model` (It holds the algorithm chosen by user)
  - A Python list containing the feature column headers, i.e.,

    `['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']`

2. Inside the `prediction()` function:

  - Call the `predict()` function on the `model` object.

  - The `predict()` function returns an array containing a single-digit integer value that would be either 1, 2, 3, 5, 6 or 7 where

    - `1` denotes the glass used for making building windows (float processed) i.e `building windows float processed`

    - `2` denotes the glass used for making building windows (non-float processed) i.e. `building windows non float processed`

    - `3` denotes the glass used for making vehicle windows (float processed) i.e. `vehicle windows float processed`

    - `4` denotes the glass used for making vehicle windows (non-float processed) i.e. `vehicle windows non float processed`

    - `5` denotes the glass used for making containers i.e. `containers`

    - `6` denotes the glass used for making tableware i.e. `tableware`

    - `7` denotes the glass used for making headlamps i.e. `headlamps`

    **Note:** There are no records for the glass-type `6` in the dataset. Nevertheless, we are still accounting for it in our code.

  - Extract the integer value using the indexing method i.e. `array_name[0]` and store it in the `glass_type` variable.

  - Return the type of glass by checking the value of `type` variable i.e.,

    - If `glass_type == 1`, then return `"building windows float processed"`

    - Else if `glass_type == 2`, then return `"building windows non float processed"`

    - Else if `glass_type == 3`, then return `"vehicle windows float processed"`

    - Else if `glass_type == 4`, then return `"vehicle windows non float processed"`

    - Else if `glass_type == 5`, then return `"containers"`

    - Else if `glass_type == 6`, then return `"tableware"`

    - Else return `"headlamp"`

3. Also mark the `prediction()` function with Streamlit decorator `@st.cache()`.

**Note:** Do not run the code shown below. It will thrown an error.
"""

# S3.1: Create a function that accepts an ML model object say 'model' and the nine features as inputs
# and returns the glass type.
@st.cache()
def prediction(model , ri , na , mg , al , si , k , ca , ba , fe):
  glass_type = model.predict([[ri , na , mg , al , si , k , ca , ba , fe]])
  glass_type = glass_type[0]
  if glass_type == 1:
    return 'building windows float processed'
  elif glass_type == 2:
    return 'building windows non float processed'
  elif glass_type == 3:
    return 'vehicle windows float processed'
  elif glass_type == 4:
    return 'vehicle windows non float processed'
  elif glass_type == 5:
    return 'containers'
  else:
    return 'headlamp'

"""Next step is to add some Streamlit code for creating our front-end.

---

#### Activity 4: Displaying Title and Sidebar Title

Now it is time to add Streamlit widgets one by one. Let us add a title and the sidebar title for our Streamlit dashboard. This can be done using the `st.title()` and `st.sidebar.title()` functions.

**Syntax:** `st.title(some_title)`
"""

# S4.1: Add title on the main page and in the sidebar.
st.title('Glass Type Predictor')
st.sidebar.title('EDA')

"""After adding the above code, run your web app using the following command:

`streamlit run glass_type_app.py`

You will see the following output:

<center><img src="https://s3-whjr-v2-prod-bucket.whjr.online/4b952189-b75d-4c1a-aa0a-ff154444a7d9.PNG"></center>

If you notice in the image above, anything we call with the sidebar object will appear in the left-hand side of the web page.

**Important points about `st.sidebar`:**

- It is used to give a cleaner look to your app by moving your widgets into the left-hand side of your screen. This keeps your app at the centre, while the widgets are pinned to the left.

- The syntax for adding any widget to the sidebar is `st.sidebar.[widget]()`

  For example: `st.sidebar.title()`, `st.sidebar.checkbox()`, `st.sidebar.slider()` etc.

**Note:** For the upcoming activities, keep appending the code in the `glass_type_app.py` file using the Sublime editor and then rerun your app on your local machine.

---

#### Activity 5: Displaying Raw Data

You can display the dataset in raw form using `st.dataframe()` function.

**Syntax:** `st.dataframe(data)` where `data` is the pandas DataFrame object.

You can even display your dataset using `st.write()` function as follows:

> `st.write(data)`

Let us also add a checkbox widget in the sidebar to display the glass-type `glass_df` DataFrame only when this checkbox is clicked. It should look like this:

<center><img src="https://s3-whjr-v2-prod-bucket.whjr.online/0b3bf6a9-8362-40ef-a0f4-c88cf5450a4f.PNG"></center>

**Syntax:** `st.checkbox(label)`

To add the checkbox in the sidebar, simply use `st.sidebar.checkbox()` instead of `st.checkbox()`.

When the user clicks on the checkbox labeled **`Show raw data`**,
- Display a subheader on the main page with a label `"Glass Type Data set"` using `st.subheader()` function.

  **Syntax: `st.subheader(some_text)`**
- Below the subheader, display raw data using `st.dataframe()` function.

**Note:** Don't run the code shown below. It will throw an error.
"""

# S5.1: Using the 'if' statement, display raw data on the click of the checkbox.
if st.sidebar.checkbox('Show Raw Data'):
  st.subheader('Full DataSet')
  st.dataframe(glass_df)

"""After running the app , it can be visualised as below:

<img src="https://s3-whjr-v2-prod-bucket.whjr.online/cdbfb5a1-fdaa-4505-b4ba-ea714733111c.PNG"/>

After displaying the raw data, let us visualise the dataset by displaying various charts and plots.

---

We will stop here. We will continue adding more functionalities to this web app using various interactive widgets in the next class.

---
"""