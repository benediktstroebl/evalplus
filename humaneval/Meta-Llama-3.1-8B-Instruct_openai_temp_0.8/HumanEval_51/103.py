### Remove Vowels from a String
#### Problem Statement
The `remove_vowels` function takes a string as input and returns the string without vowels. The function should handle vowels in both lowercase and uppercase.

#### Solution
```markdown
### Code
```python
def remove_vowels(text):
    """
    Remove vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string without vowels.

    Example:
        >>> remove_vowels('')
        ''
        >>> remove_vowels("abcdef\nghijklm")
        'bcdf\nghjklm'
        >>> remove_vowels('abcdef')
        'bcdf'
        >>> remove_vowels('aaaaa')
        ''
        >>> remove_vowels('aaBAA')
        'B'
        >>> remove_vowels('zbcd')
        'zbcd'
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

#### Explanation
This solution works by defining a string `vowels` that contains all the vowels in both lowercase and uppercase. It then uses a list comprehension to create a new string where each character is only included if it is not in the `vowels` string. Finally, it uses the `join` method to concatenate the characters into a single string.