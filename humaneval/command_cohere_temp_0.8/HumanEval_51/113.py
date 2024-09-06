Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This function removes vowels (both uppercase and lowercase) from the input text using the `translate` method with a translation table created using `str.maketrans()`. It handles various edge cases, including empty strings, strings with whitespace, and cases where the input string contains only vowels or only consonants. The intent of this code is to remove vowels from a given text, leaving only consonants. 

You can verify this by running the following tests:
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
>>> remove_vowels('Hello, World!')
'Hll, Wrd!'
```

Note: The above code assumes that the input text is comprised solely of alphabetic characters and does not contain any numeric or special characters. If the input text contained a combination of alphabetic and non-alphabetic characters, the code would require additional refinement to appropriately address the situation.