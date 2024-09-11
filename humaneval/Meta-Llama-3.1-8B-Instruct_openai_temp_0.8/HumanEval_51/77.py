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
    # Define a set of vowels to be removed
    vowels = set('aeiouAEIOU')
    
    # Use a list comprehension to filter out vowels
    # and then join the result back into a string
    return ''.join([char for char in text if char not in vowels])

# Test cases
print(remove_vowels(''))  # Should print ''
print(remove_vowels("abcdef\nghijklm"))  # Should print 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # Should print 'bcdf'
print(remove_vowels('aaaaa'))  # Should print ''
print(remove_vowels('aaBAA'))  # Should print 'B'
print(remove_vowels('zbcd'))  # Should print 'zbcd'
```

However, this can be achieved more efficiently using the `translate` method, which replaces specified characters in a string:

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
    # Create a translation table that maps vowels to None
    trans_table = str.maketrans('', '', 'aeiouAEIOU')
    
    # Use the translate method to replace vowels with None
    # and then remove the None characters
    return text.translate(trans_table)

# Test cases
print(remove_vowels(''))  # Should print ''
print(remove_vowels("abcdef\nghijklm"))  # Should print 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # Should print 'bcdf'
print(remove_vowels('aaaaa'))  # Should print ''
print(remove_vowels('aaBAA'))  # Should print 'B'
print(remove_vowels('zbcd'))  # Should print 'zbcd'
```

This version of the function is more efficient because it avoids creating a list of characters, which can be expensive for large strings.