#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

# Simulated user database
user_database = {
    "john_doe": {"password": "password123", "security_question": "What is your favorite color?", "security_answer": "blue", "phone_number": "1234567890"},
    "praveen": {"password": "praveen123", "security_question": "What is your favorite color?", "security_answer": "purple", "phone_number": "9646475890"},
    "nipun": {"password": "nipun123", "security_question": "What is your favorite color?", "security_answer": "white", "phone_number": "8088808900"},
    "faizan": {"password": "faizan123", "security_question": "What is your favorite color?", "security_answer": "red", "phone_number": "9034567890"},
    "shobin": {"password": "shobin123", "security_question": "What is your favorite color?", "security_answer": "brown", "phone_number": "6034567890"},
    "sourav": {"password": "sourav123", "security_question": "What is your favorite color?", "security_answer": "black", "phone_number": "7834567890"},
    "rahul": {"password": "rahul123", "security_question": "What is your favorite color?", "security_answer": "orange", "phone_number": "9874567890"},
    "rohit": {"password": "rohit123", "security_question": "What is your favorite color?", "security_answer": "grey", "phone_number": "7834567890"}
    
}

# Simulate sending a one-time code to the user's phone
def send_one_time_code(phone_number):
    one_time_code = random.randint(1000, 9999)
    print(f"Sent one-time code {one_time_code} to {phone_number}")
    return one_time_code

# Function to perform three-factor authentication
def three_factor_authentication(username, password):
    if username in user_database:
        if user_database[username]['password'] == password:
            phone_number = user_database[username]['phone_number']
            one_time_code = send_one_time_code(phone_number)
            user_input_code = int(input("Enter the one-time code sent to your phone: "))
            
            if user_input_code == one_time_code:
                security_question = user_database[username]['security_question']
                correct_answer = user_database[username]['security_answer']
                user_input_answer = input(f"{security_question}\nYour answer: ")

                if user_input_answer == correct_answer:
                    return True

    return False

# Simulate the three-factor authentication process
username = input("Enter your username: ")
password = input("Enter your password: ")

authentication_result = three_factor_authentication(username, password)

if authentication_result:
    print("Authentication successful!")
else:
    print("Authentication failed.")


# In[ ]:




