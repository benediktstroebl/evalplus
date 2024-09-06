Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and provides translations for removing both lowercase and uppercase vowels. The tests demonstrate the correct behavior of the function against various input scenarios.

The expected outcome for each test case is:
```
''
'bcdf\nghjklm'
'bcdf'
''
'B'
'zbcd'
```