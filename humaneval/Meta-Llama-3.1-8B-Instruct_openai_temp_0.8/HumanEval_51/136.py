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
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Test cases
if __name__ == "__main__":
    print(remove_vowels(''))
    print(remove_vowels("abcdef\nghijklm"))
    print(remove_vowels('abcdef'))
    print(remove_vowels('aaaaa'))
    print(remove_vowels('aaBAA'))
    print(remove_vowels('zbcd'))
```

This script uses a list comprehension to create a new string without vowels. It iterates over each character in the input string and checks if it is a vowel. If it is not a vowel, it is included in the new string. The `join` method is then used to concatenate the characters back into a string. 

The test cases at the end of the script demonstrate the function's behavior on various inputs.