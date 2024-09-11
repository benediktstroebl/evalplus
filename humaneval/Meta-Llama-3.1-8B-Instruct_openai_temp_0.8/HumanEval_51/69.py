```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
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
print(remove_vowels(''))  # Should print ''
print(remove_vowels("abcdef\nghijklm"))  # Should print 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # Should print 'bcdf'
print(remove_vowels('aaaaa'))  # Should print ''
print(remove_vowels('aaBAA'))  # Should print 'B'
print(remove_vowels('zbcd'))  # Should print 'zbcd'
```

This script defines a function `remove_vowels` that takes a string as input and returns a new string with all vowels removed. It uses a list comprehension to create a new list of characters that does not include vowels, and then uses the `join` method to concatenate these characters into a new string. The function is then tested with the provided example use cases.