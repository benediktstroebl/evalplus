```python
def remove_vowels(text):
    """
    Remove all vowels (both lowercase and uppercase) from a given string.

    Args:
        text (str): The input string to remove vowels from.

    Returns:
        str: The input string without vowels.
    """
    # Define a string of vowels to check against
    vowels = 'aeiouAEIOU'

    # Use a list comprehension to filter out vowels from the input string
    # The 'if char not in vowels' condition ensures only non-vowel characters are included
    without_vowels = [char for char in text if char not in vowels]

    # Join the list of characters back into a string
    return ''.join(without_vowels)


# Test cases
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

This script defines a function `remove_vowels` that takes a string input, removes all vowels (both lowercase and uppercase), and returns the resulting string. The function relies on Python's built-in string and list features to filter out vowels and join the remaining characters back into a string. The provided test cases are used to verify the function's correctness.