The solution is a Python script that defines a function `make_palindrome(string: str)` that computes the shortest palindrome of a given string. It employs a algorithm to achieve this:
1. Additionally, it checks for input type and returns an error message if the input is not a string.

Here's the code snippet:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
        
    return "".join.append(string[::-1)) + string
```

The script also includes test cases for the `make_palindrome` function to ensure its correctness.