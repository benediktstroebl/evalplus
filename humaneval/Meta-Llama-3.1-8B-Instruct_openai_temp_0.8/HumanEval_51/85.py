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
    return ''.join([c for c in text if c not in vowels])

# Example usage
print(remove_vowels('')) # Output: ''
print(remove_vowels("abcdef\nghijklm")) # Output: 'bcdf\nghjklm'
print(remove_vowels('abcdef')) # Output: 'bcdf'
print(remove_vowels('aaaaa')) # Output: ''
print(remove_vowels('aaBAA')) # Output: 'B'
print(remove_vowels('zbcd')) # Output: 'zbcd'
```

This script defines a function `remove_vowels` that takes a string `text` as input, and returns a new string without any vowels. The function uses a list comprehension to iterate over each character in the input string, and only includes characters that are not vowels (according to the `vowels` string). The resulting list of characters is then joined back into a string with the `join` method. The example usage demonstrates how to use the `remove_vowels` function with different inputs.