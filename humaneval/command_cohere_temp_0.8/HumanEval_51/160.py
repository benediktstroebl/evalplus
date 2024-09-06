Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above code defines a function `remove_vowels` that takes a string `text` as an input and returns a string without any vowels. The function uses the `translate` method to remove vowels. The `str.maketrans("", "", vowels)` creates a translation table that maps each vowel to `None`.

The script corresponds to the provided tests:
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
The first test checks whether the function `remove_vowels` successfully removes vowels from a multi-word string. The next test checks if the result is an empty string when the input contains only vowels. The test then checks whether the function successfully removes vowels from a string with uppercase vowels. The last test checks whether the function maintains the punctuations and other characters in a string when removing vowels.