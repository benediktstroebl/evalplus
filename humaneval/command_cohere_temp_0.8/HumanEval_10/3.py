Here's a Python script with a self-contained function that solves the problem using Markdown code blocks:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    # Find the position of the last palindrome suffix in the string
    n = len(string)
    for i in range(n, 0, -1):
        if is_palindrome(string[i-1:i+i]):
            break

    # Reverse the string from 0 to i and append it to the end to form a palindrome
    result = string[:i] + string[i:][::-1]
    return result
```
This script includes the two functions is_palindrome() and make_palindrome(). The is_palindrome() function takes a string as input and checks whether it is a palindrome by comparing it to its reverse. The make_palindrome() function takes a string as input and returns the shortest palindrome that starts with the input string. It does this by first identifying the position of the longest palindrome suffix in the input string and then reversing the prefix up to that position and combining it with the palindrome suffix to form the shortest palindrome.