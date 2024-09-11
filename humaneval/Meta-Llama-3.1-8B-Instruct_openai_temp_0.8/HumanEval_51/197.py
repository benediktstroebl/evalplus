### Remove Vowels from a String
```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.

    Parameters:
    text (str): The input string from which vowels are to be removed.

    Returns:
    str: The input string with all vowels removed.
    """
    vowels = 'aeiouAEIOU'  # Define all vowels in both lowercase and uppercase
    return ''.join([char for char in text if char not in vowels])  # Use list comprehension to filter out vowels

# Test cases
print(remove_vowels(''))  # Expected output: ''
print(remove_vowels("abcdef\nghijklm"))  # Expected output: 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # Expected output: 'bcdf'
print(remove_vowels('aaaaa'))  # Expected output: ''
print(remove_vowels('aaBAA'))  # Expected output: 'B'
print(remove_vowels('zbcd'))  # Expected output: 'zbcd'
```
This script defines a function `remove_vowels` that takes a string `text` as input, removes all vowels (both lowercase and uppercase) from the string, and returns the resulting string. The test cases at the end demonstrate the function's correctness by comparing its output with expected outputs.