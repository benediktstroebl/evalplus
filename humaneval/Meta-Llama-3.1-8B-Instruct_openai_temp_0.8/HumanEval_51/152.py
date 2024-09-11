```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string from which vowels are to be removed.
    
    Returns:
    str: The input string without vowels.
    
    Examples:
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

# Test the function
print(remove_vowels(''))  # Output: ''
print(remove_vowels("abcdef\nghijklm"))  # Output: 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # Output: 'bcdf'
print(remove_vowels('aaaaa'))  # Output: ''
print(remove_vowels('aaBAA'))  # Output: 'B'
print(remove_vowels('zbcd'))  # Output: 'zbcd'
```