# djangoprojects
Firstly, we are creating a folder named djangoprojects in c drive.
Next we have created a directory in djangoprojects using mkdir helloworld_project.
Now, In pycharm terminal I have created a virtual environment using python -m venv venv.
After creating a venv, I am opening the directory cd .\djangoprojects\.
Now in djangoprojects, I am activating virtual environment using venv\Scripts\activate
I have installed django using pip install django. Here we should make sure it is installed in the same location of venv.
To check weather django is installed or not we use the command django-admin version.
Now I am going to start my project using django-admin startproject helloworld_project.
Here, I am opening the helloworld_project folder using cd .\helloworld_project\.
Now, I am starting the app using django-admin startapp HelloWorld_App
Here I have added Helloworld_App in the settings.py under installed apps.
Also we have written code for views.py of HelloWorld_App. Here, In the code we will give a httpresponse of hello world message.
Next we will write code for the urls.py in the helloworld_project. 
Now we need to copy the same urls.py code and paste it in the HelloWorld_App. We will modify the code here.
I have already uploaded settings.py, views.py, helloworld_projects/urls.py, HelloWorld_App/urls.py .
Later I have executed the project using python manage.py runserver.
Then I will get a link "http://127.0.0.1:8000/" like this in output. 
If we run this "http://127.0.0.1:8000/" in the browswer it displays a message as {“Message”: “Hello World!”}
