```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    str: The string without vowels.
    """
    # Define the set of vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over each character in the input string
    for char in text:
        # If the character is not a vowel, add it to the result string
        if char not in vowels:
            result += char
    
    # Return the result string
    return result

# Test the function with the provided examples
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

This script defines a function `remove_vowels` that takes a string as input and returns the string without vowels. It uses a set to store the vowels for efficient lookups, and a string `result` to store the characters that are not vowels. The function iterates over each character in the input string, adds it to the `result` string if it's not a vowel, and returns the `result` string at the end. The script also includes the provided test cases to verify the function's correctness.