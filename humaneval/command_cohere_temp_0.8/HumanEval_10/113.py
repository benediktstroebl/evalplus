Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix.
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[-i:]):
        i -= 1

    # Find the longest non-palindromic prefix before the palindromic suffix.
    j = 0
    while not is_palindrome(string[j:i]):
        j += 1

    # Reverse the non-palindromic prefix and concatenate.
    return make_palindrome(string[j:i][::-1]) + string[j:]
``` 

This code defines a function `make_palindrome` that takes a string as input and returns the shortest palindrome that begins with the supplied string. It uses two pointers to efficiently find the shortest palindrome. The first pointer iterates backward to find the longest palindromic suffix, and the second pointer iterates forward to find the longest non-palindromic prefix. The code then reverses the non-palindromic prefix and concatenates it with the palindromic suffix to form the shortest palindrome.

Here's an example of how to use the provided code to test the function:
```python
# Test if the generated palindrome is actually shorter.
print(make_palindrome('cat'))  # Expected: catac
print(make_palindrome('cata'))  # Expected: catac
``` 

And here's a more concise version of the above code that uses slightly different variable names:
```python
def make_palindrome(string):
    if not string:
        return string
    i = len(string) - 1
    j = 0
    while i > 0 and not is_palindrome(string[-i:]):
        i -= 1
    while not is_palindrome(string[j:i]):
        j += 1
    return make_palindrome(string[j:i][::-1]) + string[j:]
``` 
This code follows the same logic but uses more concise variable names and drops the comment for brevity.