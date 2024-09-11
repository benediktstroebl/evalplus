```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    str: The string without vowels.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels('')) # ''
print(remove_vowels("abcdef\nghijklm")) # 'bcdf\nghjklm'
print(remove_vowels('abcdef')) # 'bcdf'
print(remove_vowels('aaaaa')) # ''
print(remove_vowels('aaBAA')) # 'B'
print(remove_vowels('zbcd')) # 'zbcd'
```

This script uses a list comprehension to iterate over each character in the input string, and includes it in the output string only if it's not a vowel. The `join` function is then used to concatenate the characters into a single string.