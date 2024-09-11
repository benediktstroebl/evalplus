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
    # Define a string of vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    # Use a list comprehension to filter out vowels from the input string
    # The `if char not in vowels` condition ensures characters that are not vowels are kept
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels('')) # ''
print(remove_vowels("abcdef\nghijklm")) # 'bcdf\nghjklm'
print(remove_vowels('abcdef')) # 'bcdf'
print(remove_vowels('aaaaa')) # ''
print(remove_vowels('aaBAA')) # 'B'
print(remove_vowels('zbcd')) # 'zbcd'
```

This Python script defines the `remove_vowels` function as described, which takes a string as input, removes all vowels from it, and returns the resulting string.