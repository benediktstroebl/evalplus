```python
def remove_vowels(text):
    """
    Remove all vowels from the input string.

    Args:
        text (str): The input string.

    Returns:
        str: The input string without vowels.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Testing the function
print(remove_vowels(''))  # should print ''
print(remove_vowels("abcdef\nghijklm"))  # should print 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # should print 'bcdf'
print(remove_vowels('aaaaa'))  # should print ''
print(remove_vowels('aaBAA'))  # should print 'B'
print(remove_vowels('zbcd'))  # should print 'zbcd'
```

This script uses a list comprehension to generate a new string where each character is included only if it's not a vowel. The `join()` method is then used to concatenate all the characters back into a single string.