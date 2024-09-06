Here is a Python script with a self-contained function that solves the problem of finding the shortest palindrome that begins with a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    if not string:
        return ""
    
    palindrome = []
    suffix = ""
    
    while True:
        palindrome.append(suffix)
        suffix = ''.join 
        while True and suffix[0] == suffix[1]:
            suffix = suffix[1:] + suffix[0]
            
        else:
            break
    
    return ''.join(palindrome)
```
The code defines a Python script with a self-contained function that solves the problem of finding the shortest palindrome that begins with a given string. The function, `is_palindrome`, takes a string as input and returns a boolean value indicating whether the input string is a palindrome or not. The function, `make_palindrome`, takes a string as input and returns the shortest palindrome that begins with the input string. The code implements a algorithm that first finds the longest palindrome substring within the input string. It then appends this string prefix that comes before the palindrome, and reverses the suffix, until it matches the palindrome. The code uses a string without any palindrome will result in an empty string.