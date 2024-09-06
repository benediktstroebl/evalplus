Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This removes all vowels (both lowercase and uppercase) from the text using the `translate` method with a translation table created using `str.maketrans`. It leaves other characters untouched. The argument text can be an empty string, a string with vowels, a string without vowels, or a string with uppercase vowels, and the function will return the appropriate processed string. The expected behavior for each test case is:
```
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