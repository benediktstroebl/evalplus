Here is a self-contained Python function that solves the problem of finding the shortest palindrome that begins with a supplied string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not is_palindrome(string):
        return ""  # no palindrome found

    # Algorithm idea:
    # Find the longest postfix of supplied string that is a palindrome
    postfix = ""
    while string[-1] != postfix[-1]:
        if string[-1] == postfix[-2]:
            postfix += string[-1]
        else:
            postfix += string[-1]
            string -= 1  # skip non-palindromic characters
    return postfix + string[::-1]
```
The function is designed to determine whether a given string is a palindrome, and if not, it returns "". It employs a simple algorithm that iterates through the characters of the string, comparing each character to the previous character in the postfix sequence until a match is found.

The function then constructs the shortest palindrome by appending the first character of the postfix sequence to the reverse of the characters that came before it.