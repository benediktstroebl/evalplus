```python
def remove_vowels(text):
    """
    Removes vowels from the input string.

    Args:
        text (str): The input string.

    Returns:
        str: The input string with vowels removed.
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

This Python script uses a list comprehension to create a new string that excludes vowels. The `join()` function is then used to concatenate the characters back into a single string. The test cases are included at the end to demonstrate the function's behavior.