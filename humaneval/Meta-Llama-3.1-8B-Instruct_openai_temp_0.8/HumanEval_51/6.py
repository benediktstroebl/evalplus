```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    str: The string without vowels.
    
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
    vowels = 'aeiouAEIOU'  # Define vowels in both lowercase and uppercase
    return ''.join([char for char in text if char not in vowels])  # Use list comprehension to filter out vowels

# Test the function
print(remove_vowels(''))  # Test empty string
print(remove_vowels("abcdef\nghijklm"))  # Test string with newline character
print(remove_vowels('abcdef'))  # Test string without vowels
print(remove_vowels('aaaaa'))  # Test string with only vowels
print(remove_vowels('aaBAA'))  # Test string with vowels and non-vowels
print(remove_vowels('zbcd'))  # Test string without vowels
```

This Python script defines a function `remove_vowels` that removes all vowels from a given string. It uses list comprehension to iterate over the characters in the string and includes only those that are not vowels. The function is then tested with various examples to demonstrate its correctness.