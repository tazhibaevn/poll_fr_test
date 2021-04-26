## **Тестовое задание**

Задача: спроектировать и разработать API для системы опросов пользователей

### Installation requirements

    asgiref==3.3.4
    Django==3.2
    django-filter==2.4.0
    djangorestframework==3.12.4
    Markdown==3.3.4
    python-decouple==3.4
    pytz==2021.1
    sqlparse==0.4.1

### Installation guide

    cd project/
    pip install -r requirements.txt
    cd project/
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

### API documentation

#### To get user token:

- Request method: GET
- URL: http://localhost:8000/login/
- Body:
  - username:
  - password:
- Example:
    curl --location --request GET 'http://localhost:8000/login/' \
    --form 'username=%username' \
    --form 'password=%password'

### To create poll:

- Request method: POST
- URL: http://localhost:8000/poll/
- Header:
    - Authorization: Token userToken
- Body:
    - name: name of poll
    - pub_date: publication date can be set only when poll is created, format: YYYY-MM-DD HH:MM:SS
    - end_date: poll end date, format: YYYY-MM-DD HH:MM:SS
    - description: description of poll
- Example:
  
        curl --location --request POST 'http://localhost:8000/poll/' \
        --header 'Authorization: Token %userToken' \
        --form 'name=%name' \
        --form 'pub_date=%pub_date' \
        --form 'end_date=%end_date \
        --form 'description=%description'

### To update poll:

- Request method: PUT
- URL: http://localhost:8000/poll/[poll_id]/
- Header:
  - Authorization: Token userToken
- Param:
  - poll_id
- Body:
  - name: name of poll
  - end_date: poll end date, format: YYYY-MM-DD HH:MM:SS
  - description: description of poll
- Example:
  
          curl --location --request PUT 'http://localhost:8000/poll/[poll_id]/' \
          --header 'Authorization: Token %userToken' \
          --form 'name=%poll_name' \
          --form 'end_date=%end_date \
          --form 'description=%poll_description'

### To delete poll:

- Request method: DELETE
- URL: http://localhost:8000/poll/[poll_id]/
- Header:
  - Authorization: Token userToken
- Param:
  - poll_id
- Example:
      curl --location --request GET 'http://localhost:8000/poll/[poll_id]' \
      --header 'Authorization: Token %userToken'
  

### To get list of poll:

- Request method: GET
- URL: http://localhost:8000/poll/
- Header:
- Authorization: Token userToken
- Example:
    
      curl --location --request GET 'http://localhost:8000/poll/' \
      --header 'Authorization: Token %userToken'


### To view currently active polls:

- Request method: GET
- URL: http://localhost:8000/poll/active/
- Header:
- Authorization: Token userToken
- Example:
      
      curl --location --request GET 'http://localhost:8000/poll/active/' \
      --header 'Authorization: Token %userToken'

### To create question:

- Request method: POST
- URL: http://localhost:8000/question/
- Header:
  - Authorization: Token userToken
- Body:
  - poll: id of poll
  - question_text:
  - question_type: can be only one, multiple or text
- Example:
  
      curl --location --request POST 'http://localhost:8000/question/' \
      --header 'Authorization: Token %userToken' \
      --form 'poll=%poll' \
      --form 'question_text=%question_text' \
      --form 'question_type=%question_type \

### To update question:

- Request method: PUT
- URL: http://localhost:8000/question/[question_id]/
- Header:
  - Authorization: Token userToken
- Body:
  - poll: id of poll
  - question_text:
  - question_type: can be only one, multiple or text
- Example:
  
      curl --location --request PUT 'http://localhost:8000/question/[question_id]/' \
      --header 'Authorization: Token %userToken' \
      --form 'poll=%poll' \
      --form 'question_text=%question_text' \
      --form 'question_type=%question_type \

### To delete question:

- Request method: DELETE
- URL: http://localhost:8000/question/[question_id]/
- Header:
  - Authorization: Token userToken
- Param:
  - question_id
- Example:
  
      curl --location --request DELETE 'http://localhost:8000/question/[question_id]/' \
      --header 'Authorization: Token %userToken' \
      --form 'poll=%poll' \
      --form 'question_text=%question_text' \
      --form 'question_type=%question_type \


### To get list of question:

- Request method: GET
- URL: http://localhost:8000/question/
- Header:
- Authorization: Token userToken
- Example:
    
      curl --location --request GET 'http://localhost:8000/question/' \
      --header 'Authorization: Token %userToken'


### To create choice:

- Request method: POST
- URL: http://localhost:8000/choice/
- Header:
  - Authorization: Token userToken
- Body:
  - question: id of question
  - choice_text: choice
- Example:
    
      curl --location --request POST 'http://localhost:8000/choice/' \
      --header 'Authorization: Token %userToken' \
      --form 'question=%question' \
      --form 'choice_text=%choice_text'

### To update choice:

- Request method: PUT
- URL: http://localhost:8000/choice/[choice_id]/
- Header:
  - Authorization: Token userToken
- Param:
  - choice_id
- Body:
  - question: id of question
  - choice_text: choice
- Example:
      
      curl --location --request PATCH 'http://localhost:8000/choice/[choice_id]/' \
      --header 'Authorization: Token %userToken' \
      --form 'question=%question' \
      --form 'choice_text=%choice_text'

### To delete choice:

- Request method: DELETE
- URL: http://localhost:8000/choice/[choice_id]/
- Header:
  - Authorization: Token userToken
- Param:
  - choice_id
- Example:
  
      curl --location --request DELETE 'http://localhost:8000/choice/[choice_id]/' \
      --header 'Authorization: Token %userToken' \
      --form 'question=%question' \
      --form 'choice_text=%choice_text'

### To get list of choice:

- Request method: GET
- URL: http://localhost:8000/choice/
- Header:
- Authorization: Token userToken
- Example:
    
      curl --location --request GET 'http://localhost:8000/choice/' \
      --header 'Authorization: Token %userToken'


### To create answer:

- Request method: POST
- URL: http://localhost:8000/answer/
- Header:
  - Authorization: Token userToken
- Body:
  - poll: id of poll
  - question: id of question
  - choice: if question type is one or multiple then it’s id of choice else null
  - choice_text: if question type is text then it’s text based answer else null
- Example:
      
      curl --location --request POST 'http://localhost:8000/answer/' \
      --header 'Authorization: Token %userToken' \
      --form 'poll=%poll' \
      --form 'question=%question' \
      --form 'choice=%choice \
      --form 'choice_text=%choice_text'

### To create answer:

- Request method: PUT
- URL: http://localhost:8000/answer/[answer_id]/
- Header:
  - Authorization: Token userToken
- Body:
  - poll: id of poll
  - question: id of question
  - choice: if question type is one or multiple then it’s id of choice else null
  - choice_text: if question type is text then it’s text based answer else null
- Example:
      
      curl --location --request PUT 'http://localhost:8000/answer/[answer_id]/' \
      --header 'Authorization: Token %userToken' \
      --form 'poll=%poll' \
      --form 'question=%question' \
      --form 'choice=%choice \
      --form 'choice_text=%choice_text'

### To delete answer:

- Request method: DELETE
- URL: http://localhost:8000/answer/[answer_id]/
- Header:
  - Authorization: Token userToken
- Param:
  - answer_id
- Example:
      
      curl --location --request DELETE 'http://localhost:8000/answer/[answer_id]' \
      --header 'Authorization: Token %userToken'

### To view answers of user:

- Request method: GET
- URL: http://localhost:8000/answer/[user_id]/
- Param:
  - user_id
- Header:
  - Authorization: Token userToken
- Example:
      
      curl --location --request GET 'http://localhost:8000/answer/[user_id]' \
      --header 'Authorization: Token %userToken'