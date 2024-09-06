Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above code defines a function `remove_vowels` that takes a string text as an argument and returns a string without any vowels. It uses the `translate` method to remove all occurrences of vowels from the text. The vowels to be removed are specified in the `vowels` string which supports both uppercase and lowercase vowels.

Here is a sample output:
```
>>> remove_vowels('abcdef')
'bcdf'
>>> remove_vowels('aaaaa')
''
>>> remove_vowels('aaBAA')
'B'
>>> remove_vowels('zbcd')
'zbcd'
```