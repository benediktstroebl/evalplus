```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string
    
    Returns:
    str: The input string without vowels
    """
    # Define the vowels
    vowels = 'aeiouAEIOU'
    
    # Use a generator expression with the join function to filter out vowels
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

This script uses a generator expression to filter out vowels from the input string. The `join` function is then used to concatenate the characters back into a string. This approach is efficient because it avoids creating intermediate lists or strings. Instead, it generates the characters one by one, which makes it suitable for large input strings.