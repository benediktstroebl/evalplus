```python
def remove_vowels(text):
    """
    Removes vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The input string without vowels.
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

This script uses a list comprehension to iterate over the characters in the input string and only includes characters that are not vowels. The `join()` function is then used to combine these characters into a single string. The test cases are run at the end to verify the correctness of the function.