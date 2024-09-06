Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above method uses the `str.translate()` method to remove vowels from the text. The `str.maketrans()` function is used to create a translation table that removes the vowels, and these two functions are passed to the `translate()` method to remove the vowels. This approach comprehensively removes vowels from the string.

You can test this function with the following test cases:
```python
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

This function should have the same behavior as the `remove_vowels` function described in your original prompt. Let me know if you need any adjustments.