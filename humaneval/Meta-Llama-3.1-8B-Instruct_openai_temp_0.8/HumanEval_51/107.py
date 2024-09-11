```python
def remove_vowels(text):
    """
    Removes vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string without vowels.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Test cases
if __name__ == "__main__":
    assert remove_vowels('') == ''
    assert remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert remove_vowels('abcdef') == 'bcdf'
    assert remove_vowels('aaaaa') == ''
    assert remove_vowels('aaBAA') == 'B'
    assert remove_vowels('zbcd') == 'zbcd'
    print("All test cases pass.")
```

This script defines a function `remove_vowels` that takes a string as input and returns the string without vowels. It uses a list comprehension to iterate over each character in the string and includes the character only if it is not a vowel. The `join` method is then used to concatenate the characters into a single string.

The test cases are included at the end of the script and use the `assert` statement to verify that the function behaves as expected. If all test cases pass, the script prints "All test cases pass."