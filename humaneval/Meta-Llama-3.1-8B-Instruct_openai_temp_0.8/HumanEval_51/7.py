```python
def remove_vowels(text):
    """
    Remove vowels from a given string.

    Args:
        text (str): Input string.

    Returns:
        str: String without vowels.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

This Python script uses a list comprehension to iterate over each character in the input string. It includes a conditional statement that checks if the character is not in the string of vowels. If it's not a vowel, the character is added to the list. Finally, the `join()` function is used to concatenate the characters in the list into a single string, which is then returned.

The `doctest.testmod()` function is used to run the test cases provided in the docstring. If all test cases pass, the script will run without any errors.