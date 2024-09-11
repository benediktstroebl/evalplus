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
    # Reverse the input string to easily compare prefixes and postfixes
    rev_str = string[::-1]
    
    # Initialize the longest palindromic postfix
    longest_postfix = ""
    
    # Iterate over all possible lengths of postfixes
    for i in range(len(string)):
        postfix = string[-(i+1):]
        
        # Check if the postfix is a palindrome
        if is_palindrome(postfix):
            # If it is, update the longest palindromic postfix
            longest_postfix = postfix
    
    # If no palindromic postfix was found, the input string is already a palindrome
    if not longest_postfix:
        return string
    
    # Find the length of the prefix that comes before the longest palindromic postfix
    prefix_len = len(string) - len(longest_postfix)
    
    # Reverse the prefix and append it to the end of the string
    palindrome = string + string[:prefix_len][::-1]
    
    return palindrome


# Example usage:
print(make_palindrome(""))  # Output: ''
print(make_palindrome("cat"))  # Output: 'catac'
print(make_palindrome("cata"))  # Output: 'catac'
```

This script defines two functions, `is_palindrome` and `make_palindrome`, as specified. The `make_palindrome` function uses a simple algorithm to find the shortest palindrome that begins with a given string. It works by iterating over all possible lengths of postfixes and checking if each one is a palindrome. If a palindromic postfix is found, the function updates it as the longest one found so far. If no palindromic postfix is found, the input string is already a palindrome. The function then reverses the prefix that comes before the longest palindromic postfix and appends it to the end of the string to form the shortest palindrome that begins with the input string.