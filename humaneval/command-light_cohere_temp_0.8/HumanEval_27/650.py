```python
def flip_case(string: str) -> str:
    """
    >>> flip_case('hello')  # Output: 'olleH'
    >>> flip_case('HELLO')  # Output: 'olleH'
    >>> flip_case('HELLO WORLD') # Output: 'oW rLLoW'
    >>> flip_case(' Prime') # Output: 'PRiME'
    >>> flip_case('  Hello World  ') # Output: 'oH llEoUnD'
    """
    return string.swap(c for c in string if c.isalpha())

``` 
This function flips the case of any lowercase letter in the string to an uppercase letter and vice versa. It uses the Python's `str.isalpha()` method to check if a character is an uppercase letter.