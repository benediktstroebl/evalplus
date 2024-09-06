Here's a self-contained Python function that finds and returns the shortest palindrome of a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.
    palindrome = string[::-1]
    while palindrome != string and palindrome != '':
        if is_palindrome(palindrome):
            break
        palindrome = palindrome[::-1]
    return palindrome
```
This function uses a sliding window approach to find the first palindrome, and then appends the reverse of the prefix that matches the longest palindrome suffix to the end of the original string to get the desired palindrome.