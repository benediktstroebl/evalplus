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
    prefix = string
    while not is_palindrome(prefix):
        prefix = prefix[:-1]
    
    postfix = prefix[::-1]
    return string + postfix


if __name__ == "__main__":
    test_cases = ['',
                  'cat',
                  'cata',
                 'madam',
                  'abcba',
                  'not a palindrome']
    
    for test_case in test_cases:
        print(f"Original string: {test_case}")
        print(f"Shortest palindrome: {make_palindrome(test_case)}")
        print()
```

This script first checks if the input string is a palindrome. If not, it finds the longest postfix of the string that is a palindrome, reverses the string prefix that comes before this palindromic suffix, and appends it to the end of the string. The result is a palindrome that begins with the supplied string and is the shortest possible palindrome. 

Please note that the above script creates test cases and directly prints out the results. You can easily integrate the'make_palindrome' function into your existing code and provide it with the string you'd like to check for palindrome. 

Also, note that this solution uses slicing which is efficient but may not be suitable for huge strings due to the memory requirements of slicing. For such cases, an iterative solution can be implemented instead.