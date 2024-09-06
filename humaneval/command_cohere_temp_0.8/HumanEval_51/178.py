Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above code defines a function `remove_vowels` that takes a string `text` as an argument and returns a string without any vowels. The code uses the `translate` method to remove vowels from the text. The `str.maketrans()` method creates a translation table that maps each character in `vowels` to `None` and returns the translated text.

Here's the documentation for the remove_vowels function so that you can verify its behavior:
```
remove_vowels is a function that takes a string and returns a string without vowels.
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
```

This documentation verifies that the `remove_vowels` function works accordingly and satisfies the previous tests.

This approach ensures that the resulting string has no vowels, regardless of the input text's contents or structure. 
It's a straightforward and effective method for removing vowels from a string in Python. 
It eliminates the need for additional tools like regular expressions or nested loops, making the code more understandable and efficient.