# Setup Instructions

## Requirements
1. Python 3.8 (Global Environment Variables recommended)
2. Virtual Environment (pipenv)
3. Python-ready IDE

## Installation

1. Clone this repository:

    ```sh
    $ git clone https://github.com/carlosProgrammer/Paranuara-Challenge.git
    $ cd Paranuara-Challenge
    ```

1. Create and activate virtual environment:

    ```sh
    $ python -m venv env
    $ source env/bin/activate
    ```
    >**TIP**: In a newly created virtualenv there will also be a activate shell script. For Windows systems, activation 
     scripts are provided for the Command Prompt and Powershell.                                                                                                                                                                                                                                           
    
1. Install Flask with pip:

    ```sh
    (env)$ pip install flask
    ```
   >**TIP**: This solutions works fine with older flask's versions as well.

1. Run tests:

    ```sh
    (env)$ python test.py
    ```
       
1. Run app:

    ```sh
    (env)$ python app.py
    ```
   
   >**TIP** You can use different .json files, however filenames are hard coded. Keep that in mind

## Interaction with the System via URLS

1. Get employees of given company name:

    ```
    http://127.0.0.1:5000/paranuara/api/v1.0/company/<company_name>
    ```
    
    Ex.
    ```
    http://127.0.0.1:5000/paranaura/api/v1.0/company/LINGOAGE
    ```
    
1. Get common friends for given two people:

    ```
    http://127.0.0.1:5000/paranaura/api/v1.0/people/<id1>/<id2>
    ```
    
    Ex.
    ```
    http://127.0.0.1:5000/hivery/api/v1.0/people/678/520
    ```
    
1. Get 1 people's info including favourite fruits and vegetables info:

    ```
    http://127.0.0.1:5000/hivery/api/v1.0/people/<id>
    ```
    
    Ex.
    ```
    http://127.0.0.1:5000/hivery/api/v1.0/people/100
    ```
 
    
