Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels (both uppercase and lowercase) from the input text using the `translate` method with a translation table created using `str.maketrans`. This approach ensures that all occurrences of vowels are removed while maintaining the integrity of the text's punctuation and other characters.

The test cases are included to validate the function's behavior:
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

Feel free to modify the script to better suit your needs or improve its efficiency, it is a straightforward solution for this problem.