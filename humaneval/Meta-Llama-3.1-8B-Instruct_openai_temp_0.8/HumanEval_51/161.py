```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.

    Args:
        text (str): The input string.

    Returns:
        str: The string without vowels.
    """
    # Define vowels in both lowercase and uppercase
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to iterate over the input string
    # and only include characters that are not vowels
    text_without_vowels = ''.join([char for char in text if char not in vowels])
    
    return text_without_vowels

# Test cases
if __name__ == "__main__":
    print(remove_vowels(''))  # Should print: ''
    print(remove_vowels("abcdef\nghijklm"))  # Should print: 'bcdf\nghjklm'
    print(remove_vowels('abcdef'))  # Should print: 'bcdf'
    print(remove_vowels('aaaaa'))  # Should print: ''
    print(remove_vowels('aaBAA'))  # Should print: 'B'
    print(remove_vowels('zbcd'))  # Should print: 'zbcd'
```

This Python script defines a `remove_vowels` function that takes a string as input and returns the string without vowels. The function uses a list comprehension to filter out vowels (both lowercase and uppercase) from the input string. The filtered string is then returned by the function. The script includes test cases to verify that the function behaves correctly for different inputs.