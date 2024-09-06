Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans`. This approach ensures that all vowels (both lowercase and uppercase) are removed regardless of the input case. The tests provided will verify the correct removal of vowels from different input scenarios.

The expected output for each test case is:
```
''
'bcdf\nghjklm'
'bcdf'
''
'B'
'zbcd'
```