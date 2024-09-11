```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    
    :param string: The input string
    :return: The shortest palindrome starting with the input string
    """
    # Find the longest suffix of the string that is a palindrome
    for i in range(len(string), 0, -1):
        suffix = string[-i:]
        if is_palindrome(suffix):
            # Remove the palindromic suffix from the string
            prefix = string[:-i]
            # Append the reverse of the prefix to the end of the string
            palindrome = string + prefix[::-1]
            return palindrome

    # If no palindromic suffix is found, return an empty string
    return ''


# Test cases
if __name__ == "__main__":
    assert is_palindrome('') == True
    assert is_palindrome('') == True
    assert make_palindrome('') == ''
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'
```

This script first defines the `is_palindrome` function to test if a given string is a palindrome. Then it defines the `make_palindrome` function to find the shortest palindrome that begins with a supplied string. The function works by finding the longest postfix of the string that is a palindrome, and then appending to the end of the string the reverse of the prefix that comes before the palindromic suffix. The script includes test cases to verify the correctness of the functions.