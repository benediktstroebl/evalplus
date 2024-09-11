```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    Vowels are considered as 'a', 'e', 'i', 'o', 'u' in both lower and upper case.
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
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

This script uses list comprehension to iterate over each character in the string and checks if the character is a vowel. If it's not a vowel, it's included in the new string. The `join()` function is then used to combine all characters in the list into a single string.