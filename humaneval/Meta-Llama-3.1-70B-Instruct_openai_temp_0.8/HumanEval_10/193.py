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
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        postfix = string[i-1:]
        if is_palindrome(postfix):
            prefix = string[:i-1]
            return string + prefix[::-1]


# Run the tests
test_cases = [
    ['', ''],
    ['cat', 'catac'],
    ['cata', 'catac']
]
for input_string, expected_output in test_cases:
    output = make_palindrome(input_string)
    if output == expected_output:
        print(f'Test passed for {input_string}: {output}')
    else:
        print(f'Test failed for {input_string}. Expected {expected_output}, got {output}.')
```