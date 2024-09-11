```python
def remove_vowels(text):
    """
    Remove all vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string without vowels.
    """
    # Define the set of vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')

    # Use a list comprehension to filter out vowels from the string
    # The if condition checks if a character is not in the set of vowels
    filtered_chars = [char for char in text if char not in vowels]

    # Join the filtered characters back into a string
    result = ''.join(filtered_chars)

    return result

# Test the function
print(remove_vowels(""))  # Empty string
print(remove_vowels("abcdef\nghijklm"))  # Remove vowels from a multi-line string
print(remove_vowels("abcdef"))  # Single line string
print(remove_vowels("aaaaa"))  # String with only vowels
print(remove_vowels("aaBAA"))  # String with both lowercase and uppercase vowels
print(remove_vowels("zbcd"))  # String without vowels
```

This script defines a function `remove_vowels` that takes a string as input and returns the string without vowels. It uses a list comprehension to filter out vowels from the input string and then joins the remaining characters back into a string using the `join` method. The script also includes test cases to demonstrate the function's behavior.