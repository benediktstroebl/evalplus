Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "AEIOUaeiou"
    return text.translate(str.maketrans("", "", vowels))
```

This removes all vowels, both uppercase and lowercase, from the input text. It uses the `translate` method with a custom translation table created using `str.maketrans` to remove all instances of vowels from the text. The result is a string that has all vowels removed, and its length is reduced, as evidenced by the following tests:
```python
>>> remove_vowels('abcdef')
'bcdf'
>>> remove_vowels('aaaaa')
''
>>> remove_vowels('aaBAA')
'B'
>>> remove_vowels('zbcd')
'zbcd'
```