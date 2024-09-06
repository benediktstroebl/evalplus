Here's a self-contained Python function that checks whether a given string is a palindrome:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    if not is_palindrome(string):
        return ""  # Return an error message or empty string

    # Find the longest postfix of supplied string that is a palindrome
    postfix = ""
    for char in string:
        if char == postfix[-1] or is_palindrome(postfix[-1] + char):
            postfix += char
        else:
            break

    # Append to the string reverse of a string prefix that comes before the palindromic suffix
    return postfix + string[::-1]
```

This function uses the **is_palindrome** helper function to quickly determine whether a substring is a palindrome, and then employs a straightforward algorithm to generate the shortest palindrom.