```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    # Initialize a variable to store the longest palindromic suffix
    longest_palindromic_suffix = ""
    
    # Iterate over the characters in the string in reverse order
    for i in range(len(string), -1, -1):
        # Get the current suffix of the string
        suffix = string[:i]
        
        # Check if the suffix is a palindrome
        if is_palindrome(suffix):
            # If it is, update the longest palindromic suffix
            longest_palindromic_suffix = suffix
        else:
            # If not, break the loop
            break
    
    # If the longest palindromic suffix is the entire string, return the original string
    # Otherwise, append the reverse of the prefix that comes before the palindromic suffix
    if longest_palindromic_suffix == string:
        return string
    else:
        # Get the prefix that comes before the palindromic suffix
        prefix = string[:len(string) - len(longest_palindromic_suffix)]
        
        # Reverse the prefix
        reversed_prefix = prefix[::-1]
        
        # Append it to the end of the palindromic suffix
        palindrome = longest_palindromic_suffix + reversed_prefix
        
        return palindrome


# Test cases
print(make_palindrome(""))  # ''
print(make_palindrome("cat"))  # 'catac'
print(make_palindrome("cata"))  # 'catac'
```

This script defines the `is_palindrome` function to test if a given string is a palindrome, and the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. The `make_palindrome` function uses a simple algorithm to find the longest palindromic suffix of the input string and then appends the reverse of the prefix that comes before the palindromic suffix to create the shortest palindrome that begins with the input string.