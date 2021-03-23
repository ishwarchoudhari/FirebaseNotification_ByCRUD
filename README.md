# FirebaseNotification_ByCRUD
FirebaseCRUD
This project was generated with Python Flask.

Development server
Run  for a dev server. Navigate to http://127.0.0.1:5000/. The app will automatically reload if you change any of the source files.

Flask Firebase REST API

This application includes a is a sample Flask app that uses firebase db
Data is loaded from a cvs file to firebase
The purpose of the app is to CRUD this data through an API
Before we begin, you need a firebase account. Then you need to create a project -find this [in the console here](https://console.firebase.google.com). Then we need to collect all the config values we need to run the application:


 
You can find all these values, going to your project, then to Authentication on the left side menu (as of october 2017 console interface)
and on the top right you should see a 'WEB SETUP' button. There you will find all these values

 
 | Config&nbsp;Value  | Description |
 | :-------------  |:------------- |
ApiKey | Your primary Firebase project  identifier - (https://console.firebase.google.com/u/0/YOURPROJECTID/settings/general).
AuthDomain | Used to authenticate.
DatabaseURL | The url to access your database.
StorageBucke | We might need not need this (as of the first objective[simple api crud]), but if you want to follow along, please copy this too.


# Requirements

-  [Python3.7](https://www.python.org/downloads/) 
-  [Flask](https://github.com/pallets/flask) 
-  [Firebase Admin Python SDK](https://github.com/firebase/firebase-admin-python) 
