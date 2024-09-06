Here's the function to make a palindrome:
```python
def make_palindrome(string):
    """ Finds the shortest palindrome that begins with a supplied string.
    Algorithm idea simple: 
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    Returns a strategy ensures a shortest palindrome with the least extra characters.
    """
    Palindrome: < palindrome = input >
    string = input + string[::-1][::-1]
    return palindrome
```

You can use this function with your test strings from the previous prompt.