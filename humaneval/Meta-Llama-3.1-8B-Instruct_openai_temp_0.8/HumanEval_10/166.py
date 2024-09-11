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
    # Find the longest postfix of supplied string that is a palindrome
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left]!= string[right]:
            break
        left += 1
        right -= 1

    # If we found a palindrome, reverse the prefix and append it
    if left >= right:
        return string + string[::-1]

    # Otherwise, return the string with the reverse of the palindrome suffix appended
    return string + string[right+1:][::-1]


# Test cases
if __name__ == "__main__":
    test_cases = [
        '',
        'cat',
        'cata',
        'abcdedcba',
        'notapalindrome',
    ]

    for test_string in test_cases:
        print(f"Original string: {test_string}")
        print(f"Palindrome: {make_palindrome(test_string)}")
        print(f"Is palindrome: {is_palindrome(make_palindrome(test_string))}")
        print()
```

This script defines the `is_palindrome` and `make_palindrome` functions. The `make_palindrome` function uses a two-pointer approach to find the longest postfix of the supplied string that is a palindrome, then appends the reverse of the remaining prefix to form the shortest palindrome that begins with the supplied string. The script also includes test cases to verify the correctness of the functions.