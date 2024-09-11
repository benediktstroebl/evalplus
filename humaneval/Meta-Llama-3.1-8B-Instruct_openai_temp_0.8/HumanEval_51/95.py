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
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

In this script, the `remove_vowels` function uses a list comprehension to iterate over each character in the input string. If the character is not a vowel (i.e., it's not in the string of vowels), it's included in the new string. The `''.join(...)` expression is then used to concatenate the characters into a single string, which is then returned by the function.