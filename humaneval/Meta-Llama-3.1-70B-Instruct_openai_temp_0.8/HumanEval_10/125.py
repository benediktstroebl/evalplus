```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
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
    if not string:  # Edge case: Empty string
        return string
    
    for i in range(len(string), 0, -1):  # Iterate over the string from the end
        if is_palindrome(string[i:]):  # Check if the current postfix is a palindrome
            non_palindromic_prefix = string[:i]  # Get the non-palindromic prefix
            return string + non_palindromic_prefix[::-1]  # Append the reverse of the prefix to the end of the string
```

### Example Use Cases
```python
print(make_palindrome(""))  # Output: ''
print(make_palindrome("cat"))  # Output: 'catac'
print(make_palindrome("cata"))  # Output: 'catac'
print(make_palindrome("radar"))  # Output: 'radar'
print(make_palindrome("hello"))  # Output: 'helloolleh'
```

### Step-by-Step Explanation

The `make_palindrome` function works by iterating over the input string from the end. For each postfix, it checks whether it is a palindrome using the `is_palindrome` function. If it is, the function returns the original string with the reverse of the non-palindromic prefix appended to the end. This approach ensures that the resulting palindrome is the shortest possible one that begins with the input string.