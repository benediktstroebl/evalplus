```python
def remove_vowels(text):
    """
    Remove vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The input string without vowels.
    """
    # Define the vowels in both lowercase and uppercase
    vowels = 'aeiouAEIOU'
    
    # Use a generator expression to filter out vowels from the input string
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

This script uses a generator expression to iterate over each character in the input string and keeps only those characters that are not vowels. The `join` method is then used to concatenate the remaining characters into a single string.