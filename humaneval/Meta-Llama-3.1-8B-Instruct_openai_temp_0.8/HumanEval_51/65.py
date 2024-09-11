```python
import re

def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): input string
    
    Returns:
    str: string without vowels
    
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
    # Remove lowercase vowels
    text = re.sub('[aeiou]', '', text)
    # Remove uppercase vowels
    text = re.sub('[AEIOU]', '', text)
    return text

# Test the function
print(remove_vowels(''))
print(remove_vowels("abcdef\nghijklm"))
print(remove_vowels('abcdef'))
print(remove_vowels('aaaaa'))
print(remove_vowels('aaBAA'))
print(remove_vowels('zbcd'))
```

This script uses the `re.sub()` function from Python's built-in `re` module, which replaces occurrences of a regular expression in a string with a replacement string. The regular expression `[aeiou]` matches any lowercase vowel, and `[AEIOU]` matches any uppercase vowel. The `re.sub()` function is called twice to remove both lowercase and uppercase vowels.