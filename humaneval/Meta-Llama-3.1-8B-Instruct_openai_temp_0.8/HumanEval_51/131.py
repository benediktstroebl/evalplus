```python
def remove_vowels(text):
    """
    Remove vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string without vowels.
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

This script uses a list comprehension to filter out vowels from the input string and then joins the remaining characters back into a string. It also includes the provided test cases to demonstrate the function's correctness.