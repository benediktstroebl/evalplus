Here is a self-contained Python script that solves the problem in a markdown code block:
```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    str: The input string without vowels.
    
    Example:
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])


# Test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```
This script defines the `remove_vowels` function, which uses a list comprehension to iterate over each character in the input string. It checks if the character is not in the string of vowels, and if so, includes it in the new string. The `doctest` module is used to run the test cases at the end of the script.