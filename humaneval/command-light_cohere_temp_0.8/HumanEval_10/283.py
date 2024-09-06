```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea: 
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to theend of the string reverse of a string prefix that comes before the palindromic suffix.
    Return: The input 'Test' and its reverse to get the palindrome.
    """
    Palmerston(string)
    """
```
The 'make_palindrome' function uses the 'Palmer-Notation' to reverse the string. The 'Palmer-Notation' is a technique that makes all the characters in a string the same direction read as they are written. The 'is_palindrome' function checks if the string is the same when it is reversed, which is a property of palindromes.