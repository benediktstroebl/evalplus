```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels
    Returns: string without vowels
    """
    return ''.join(c for c in text if c.isalpha(97, 59, 65, 123, 91))

# Tests
assert remove_vowels('') == ''
assert remove_vowels('abcdef\nghijklm') == 'bcdf\nghjklm'
assert remove_vowels('abcdef') == 'bcdf'
assert remove_vowels('aaaaa') == ''
assert remove_vowels('aaBAA') == 'B'
assert remove_vowels('zbcd') == 'zbcd'
```
This script defines a function `remove_vowels` that takes a string as input and returns a new string without any vowels. The function uses a string `alpha` to check if a character is a vowel, and returns a new string with no vowels.