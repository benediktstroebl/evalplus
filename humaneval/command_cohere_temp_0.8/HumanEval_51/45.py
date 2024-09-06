Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans`. This approach ensures that all possible vowels, both lowercase and uppercase, are removed from the text.

You can verify the functionality with the following tests:
```python
remove_vowels("")
remove_vowels("abcdef\nghijklm")
remove_vowels("abcdef")
remove_vowels("aaaaa")
remove_vowels("aaBAA")
remove_vowels("zbcd")
```

The expected outputs are:
```python
''
'bcdf\nghjklm'
'bcdf'
''
'B'
'zbcd'
```