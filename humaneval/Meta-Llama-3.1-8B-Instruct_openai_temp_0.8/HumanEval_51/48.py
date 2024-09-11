```python
def remove_vowels(text):
    """
    Remove vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string without vowels.
    """
    # Define the set of vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')
    
    # Use a list comprehension to iterate over each character in the string
    # and include it in the new string only if it's not a vowel
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

This script defines a function `remove_vowels` that takes a string `text` as input and returns a new string without vowels. The function uses a set of vowels to efficiently check each character in the input string. The test cases at the end demonstrate the function's behavior with various inputs.