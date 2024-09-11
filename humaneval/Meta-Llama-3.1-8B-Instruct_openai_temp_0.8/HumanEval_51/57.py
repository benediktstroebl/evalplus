Here is a Python script that defines the `remove_vowels` function and includes the provided docstring:
```markdown
### remove_vowels Function

This script defines a function called `remove_vowels` that removes all vowels from a given string.

#### Code

```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
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
    # Define a function to check if a character is a vowel
    def is_vowel(char):
        return char.lower() in 'aeiou'

    # Use a list comprehension to iterate over the characters in the text
    # and only include characters that are not vowels
    return ''.join(char for char in text if not is_vowel(char))

# Example usage:
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```
#### Explanation

This script uses a helper function called `is_vowel` to check if a character is a vowel. The `remove_vowels` function then uses a list comprehension to iterate over the characters in the text and only include characters that are not vowels. The `join` method is used to combine the characters back into a string.