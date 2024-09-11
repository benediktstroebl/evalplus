```python
def remove_vowels(text):
    """
    Removes vowels from the input string.

    Args:
        text (str): The input string.

    Returns:
        str: The string without vowels.
    """
    # Define a string of vowels to check against
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to create a new string without vowels
    # The if condition checks if each character in the string is not in vowels
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

This script defines a function `remove_vowels` that takes a string as input and returns a new string with all vowels removed. The function uses a list comprehension to create a new string where each character is checked to see if it is not in the string of vowels. If it is not a vowel, the character is included in the new string. The test cases are then run to demonstrate the function's behavior.