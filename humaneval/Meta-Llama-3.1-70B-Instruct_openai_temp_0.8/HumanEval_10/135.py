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
    """
    # Handle edge case where the input string is empty
    if not string:
        return ''

    # Find the longest postfix of the string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[i - 1:]
        if is_palindrome(postfix):
            # Find the prefix that comes before the palindromic suffix
            prefix = string[:len(string) - len(postfix)]
            # Return the shortest palindrome that begins with the supplied string
            return string + prefix[::-1]

    # If no palindromic postfix is found, return the string with its reverse appended
    return string + string[::-1]


# Example usage
if __name__ == "__main__":
    print(make_palindrome(''))  # Output: ''
    print(make_palindrome('cat'))  # Output: 'catac'
    print(make_palindrome('cata'))  # Output: 'catac'
```