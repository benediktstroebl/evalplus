```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""

    # Find the longest postfix of supplied string that is a palindrome
    palindrome = ""
    for char in string:
        if char == palindrome[1::]:
            palindrome = char + palindrome[::-1]
        else:
            palindrome += char

    return palindrome[::-1]
```
This Python code defines two functions, is_palindrome and make_palindrome, to solve the problem of checking if a given string is a palindrome and to generate the shortest palindrome that starts with a given string, respectively.

The is_palindrome function uses the basic definition of a palindrome, which is a sequence that reads the same backwards and forwards. 

The make_palindrome function implements the algorithm for generating the shortest palindrome that starts with a given string. The algorithm works by first finding the longest postfix of the string that is a palindrome and then appending the reverse of the string prefix to the end of the postfix to create the palindrome.