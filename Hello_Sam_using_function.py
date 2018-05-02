"""
Taking data from the user and using it in our statement using functions
"""

def main():
    name = get_username();
    hello(name);

def get_username():
    user_name = input("Enter user name:");
    return user_name;

def hello(user_name):
    print("Hello",user_name,"!!!");

#Main program starts from here
main();
