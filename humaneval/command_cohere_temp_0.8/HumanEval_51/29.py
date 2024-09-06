Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above code defines a function `remove_vowels` that takes a string `text` as an argument and returns a string without any vowels. The function uses the `translate` method to remove vowels. The `str.maketrans("", "", vowels)` creates a translation table that maps each vowel to `None`.

The behavior of the function is demonstrated by the following tests:
```python
>>> remove_vowels('abcdef')
'bcdf'
>>> remove_vowels('aaaaa')
''
>>> remove_vowels('aaBAA')
'B'
>>> remove_vowels('zbcd')
'zbcd'
>>> remove_vowels('abcdef\nghijklm')
'bcdf\nghjklm'
```

The tests prove that the function appropriately eliminates vowels from diverse input texts while maintaining the spacing and other non-vowel characters.