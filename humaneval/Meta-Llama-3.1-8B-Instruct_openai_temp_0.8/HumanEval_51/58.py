```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.

    Parameters:
    text (str): the input string.

    Returns:
    str: the string without vowels.
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

This script defines a function `remove_vowels` that takes a string `text` as input and returns a new string with all vowels removed. The function uses a list comprehension to iterate over each character in the string, and only includes characters that are not vowels. The `join` function is then used to concatenate the remaining characters into a single string.

The test cases at the end of the script demonstrate the function's behavior with different inputs.