```python
def remove_vowels(text):
    """
    Remove vowels from a given string.

    Args:
    text (str): The string from which vowels are to be removed.

    Returns:
    str: The string without vowels.
    """
    # Define vowels in both lowercase and uppercase
    vowels = 'aeiouAEIOU'
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over each character in the string
    for char in text:
        # Check if the character is not a vowel
        if char not in vowels:
            # If it's not a vowel, add it to the result
            result += char
    
    # Return the string without vowels
    return result

# Test cases
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```