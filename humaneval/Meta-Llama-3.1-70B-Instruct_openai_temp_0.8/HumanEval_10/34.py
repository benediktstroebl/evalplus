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
    
    Examples:
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if is_palindrome(string):
        return string
    
    # Initialize variables to store the result and longest palindromic suffix
    result = string
    longest_palindromic_suffix = ""
    
    # Iterate through the string from the end
    for i in range(len(string), 0, -1):
        suffix = string[i-1:]
        
        # Check if the suffix is a palindrome
        if is_palindrome(suffix):
            longest_palindromic_suffix = suffix
            break
    
    # Find the prefix preceding the longest palindromic suffix
    prefix = string[:-len(longest_palindromic_suffix)]
    
    # Append the reverse of the prefix to the original string
    result += prefix[::-1]
    
    return result


# Example usage
if __name__ == "__main__":
    print(make_palindrome(""))  # Output: ''
    print(make_palindrome("cat"))  # Output: 'catac'
    print(make_palindrome("cata"))  # Output: 'catac'
```