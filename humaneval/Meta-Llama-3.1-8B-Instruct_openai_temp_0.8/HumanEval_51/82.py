### Remove Vowels from a String
```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Args:
    text (str): The input string.

    Returns:
    str: The input string without vowels.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```
This script defines a function `remove_vowels` that uses a list comprehension to filter out vowels from the input string. The `join` function is then used to combine the characters back into a single string.