```python
def remove_vowels(text):
    """
    Remove all vowels from the given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string without vowels.
    """
    vowels = 'aeiouAEIOU'  # Define all vowels
    return ''.join([char for char in text if char not in vowels])  # Use list comprehension to filter out vowels


# Test cases
if __name__ == "__main__":
    print(remove_vowels(''))  # ''
    print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
    print(remove_vowels('abcdef'))  # 'bcdf'
    print(remove_vowels('aaaaa'))  # ''
    print(remove_vowels('aaBAA'))  # 'B'
    print(remove_vowels('zbcd'))  # 'zbcd'
```

In this script, we define a function `remove_vowels` that uses list comprehension to filter out vowels from the input string. The vowels are defined in a string `vowels`. We then use the `join` method to concatenate the characters that are not vowels into a single string.

The test cases at the end of the script demonstrate the function's behavior with different inputs.