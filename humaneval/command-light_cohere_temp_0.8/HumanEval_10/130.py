Here is a self-contained Python script that defines a function is_palindrome that checks if a given string is a palindrome:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""
    else:
        return "".joinend(string[::-1] + string[:-1])
```

This function takes a string str and returns 'true' if it's a palindrome, and 'false' otherwise. The make_palindrome function then takes a string str and returns the shortest palindrome that begins with the given string. 

The function works by first checking if the input string is already a palindrome. If so, it returns an string with nothing appended, indicating that it was already a palindrome. Otherwise, it finds the longest postfix of the string that is a palindrome, and reverses it. Then, it appends the end() with the reversed prefix, followed by the first character of the original string.