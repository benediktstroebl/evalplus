Here's the function to check if a given string is a palindrome:
```python
def is_palindrome(string):
    return string == string[::-1]
```

This function simply compares the original string with its reverse to check if it's a palindrome. 

You can use this function with any string you want to test, and it will return True if they are equal, indicating it's a palindrome, and False otherwise.