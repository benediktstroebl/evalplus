```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.

    Args:
        text (str): Input string.

    Returns:
        str: String without vowels.

    Example:
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
if __name__ == "__main__":
    assert remove_vowels('') == ''
    assert remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert remove_vowels('abcdef') == 'bcdf'
    assert remove_vowels('aaaaa') == ''
    assert remove_vowels('aaBAA') == 'B'
    assert remove_vowels('zbcd') == 'zbcd'
    print("All test cases passed.")
```

This script defines a function `remove_vowels` that takes a string `text` as input and returns a new string with all vowels removed. The function uses a list comprehension to iterate over each character in the input string, and includes only those characters that are not in the string of vowels. The result is then joined back into a string. The script also includes test cases to verify that the function works correctly.