Here's a self-contained Python script that solves the given problem:
```markdown
### Remove Vowels from a String
#### Problem Statement
Remove all vowels from a given string, ignoring case.

#### Solution

```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): Input string
    
    Returns:
    str: String without vowels
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Example Usage
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

#### Explanation
This solution uses a list comprehension to iterate over each character in the input string. If a character is not a vowel (as defined by the `vowels` string), it is included in the new string. The `join()` method is then used to concatenate the characters into a single string.