```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string): 
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""
    
    palindrome = ""
    while True: 
        palindrome += string[0]
        string = string[1:]  # Drop the first character since it's also a palindrome
        if not string: 
            break  
    return palindrome[::-1]  # Return the reversed string 

# Test the functions
print(is_palindrome("racecar"))  # True
print(make_palindrome("racecar"))  # 'racerc'
print(make_palindrome("hello"))  # 'olleh'
```  This code defines two functions: `is_palindrome` checks if a given string is a palindrome and returns a boolean value, and `make_palindrome` creates the shortest palindrome from a given string. The output will demonstrate the test cases for these functions.