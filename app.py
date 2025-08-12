# app.py

def insecure_function(user_input):
    """
    This is an example of an insecure function that is vulnerable to
    command injection. Never use user input directly in shell commands.
    """
    import os
    os.system(f"echo {user_input}")  # Insecure use of user input

def secure_function(user_input):
    """
    This function uses proper sanitization and is secure.
    """
    import subprocess
    safe_input = user_input.replace(";", "").replace("&", "")  # Simple sanitization
    subprocess.run(["echo", safe_input])

if __name__ == "__main__":
    user_input = input("Enter a command: ")
    insecure_function(user_input)  # Vulnerable function call
    secure_function(user_input)    # Secure function call

