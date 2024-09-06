A simple Python script with a self-contained function that solves the problem is shown below:

```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""
    palindrome = ""
    while string:
        palindrome += string[0]
        string = string[1:]
    return palindrome
```

The two functions, **`is_palindrome`** and **`make_palindrome`**, are defined in this code. The **`is_palindrome`** function returns true if the string is a palindrome and false otherwise. The **`make_palindrome`** function creates a palindrome by locating the first character of the input string and then repeating it to the end of the string, while removing non-palindrome characters.