```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to end of the string reverse of a string prefix that comes before the palindromic suffix.
    Returns: the following code:
    - In Python 3.6, string. time series are of many implementation of the `make_palindrome` function is complete.
    - It output is the function with a sample input:
    > make_palindrome('')
        ''
    - With another sample input:
        > make_palindrome('cat')
        'catac'
    - The output of the function for all other sample inputs is the same, which is the shortest palindrome starting with the input string.
```