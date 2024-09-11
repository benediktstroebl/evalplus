```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ''
    
    for i in range(len(string), 0, -1):
        postfix = string[len(string) - i:]
        prefix = string[:len(string) - i]
        if is_palindrome(postfix):
            return string + prefix[::-1]
    
    raise ValueError("String cannot be made into a palindrome")


# Example usage
if __name__ == '__main__':
    print(make_palindrome(''))  # Output: ''
    print(make_palindrome('cat'))  # Output: 'catac'
    print(make_palindrome('cata'))  # Output: 'catac'
```

This Python script first checks if the input string is empty. If it's not empty, it tries to find the longest palindromic postfix of the string. This is achieved by iterating over the length of the string and checking each postfix (from the longest to the shortest) if it's a palindrome. If a palindromic postfix is found, the function appends the reverse of the string prefix (that comes before the palindromic suffix) to the end of the string and returns the resulting shortest palindrome. If no palindromic postfix is found, the function raises a ValueError.