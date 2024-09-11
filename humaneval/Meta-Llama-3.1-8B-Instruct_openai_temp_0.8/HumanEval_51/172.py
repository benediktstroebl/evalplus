Here's a Python script that implements the `remove_vowels` function as specified:
```markdown
### Python Script: remove_vowels Function

```python
def remove_vowels(text):
    """
    Removes vowels from the input string.
    
    Args:
        text (str): The input string.
    
    Returns:
        str: The input string without vowels.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

### Explanation

The `remove_vowels` function uses a list comprehension to generate a new string without vowels. It iterates over each character in the input string and includes it in the new string only if it's not a vowel. The resulting list of characters is then joined into a single string using the `join` method.

### Notes

* This implementation uses a pre-computed string `vowels` to store the vowels in both lowercase and uppercase.
* The list comprehension is a concise way to filter the input string.
* The `join` method is used to concatenate the characters into a single string.