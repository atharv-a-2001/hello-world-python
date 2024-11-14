# hello.py

# Function to greet the user
def greet(name):
    greeting = f"Hello, {name}!"  # Create a greeting message
    return greeting

# Main code execution
if __name__ == "__main__":
    user_name = "World"  # Assign the name
    message = greet(user_name)  # Call the greet function
    print(message)  # Print the greeting message

