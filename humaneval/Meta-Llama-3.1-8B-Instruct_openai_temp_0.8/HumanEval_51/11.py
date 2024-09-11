```markdown
# Remove Vowels Function
========================

A Python function that removes vowels from any given string.

### Code

```python
def remove_vowels(text):
    """
    Remove vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string without vowels.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Example Use Cases
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

### Explanation

This function uses a list comprehension to iterate over each character in the input string. It checks if the character is not in the string of vowels, and if so, it includes it in the new string. Finally, it returns the new string without vowels. The `join()` function is used to concatenate the characters into a single string.

### Notes

* This function treats 'y' as a consonant, not a vowel. If you want to include 'y' as a vowel, simply add it to the `vowels` string.
* This function preserves the original case of the characters in the input string. If you want to force all characters to lowercase or uppercase, you can modify the function accordingly.