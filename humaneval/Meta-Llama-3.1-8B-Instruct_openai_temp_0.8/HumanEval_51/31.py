```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    Vowels are 'a', 'e', 'i', 'o', 'u' in a case-insensitive manner.
    
    Parameters:
    text (str): The input string from which vowels will be removed.
    
    Returns:
    str: The input string without vowels.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

This script defines a function `remove_vowels` that takes a string as input and returns a new string without vowels. It uses a list comprehension to iterate over each character in the input string, and includes only the characters that are not vowels. The `join` method is then used to concatenate the characters back into a string. The script also includes the test cases from the problem description to demonstrate the function's behavior.