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

# Test cases
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

This Python script uses a list comprehension to filter out vowels from the input string. It defines the `remove_vowels` function which takes a string as input and returns a new string with all vowels removed. The function uses a string `vowels` contains all the vowels (both lowercase and uppercase). It then uses a list comprehension to create a new list of characters that are not in the `vowels` string. Finally, it uses the `join` method to concatenate the characters in the list into a string. The script also includes the test cases from the docstring to verify that the function works correctly.