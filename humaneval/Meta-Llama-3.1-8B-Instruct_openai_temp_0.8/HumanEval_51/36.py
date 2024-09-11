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
    # Define vowels as a set of lowercase and uppercase letters
    vowels = set('aeiouAEIOU')
    # Use a list comprehension to filter out vowels from the string
    # The `join` function is used to concatenate the filtered characters back into a string
    return ''.join([char for char in text if char not in vowels])

# Test the function
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

This script defines a function `remove_vowels` that takes a string as input, removes all vowels from the string, and returns the resulting string. It uses a list comprehension to filter out the vowels from the string, and the `join` function to concatenate the filtered characters back into a string. The script then tests the function with the provided test cases.