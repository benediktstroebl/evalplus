Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels (both uppercase and lowercase) from the input text using the `translate` method with a translation table created using `str.maketrans`. This approach ensures that all occurrences of vowels are removed while maintaining the relative positions of non-vowel characters. The tests provided for the function are included as part of the code block, illustrating the expected input-output scenarios. 

The test cases can be executed by adding the following code after the function definition:
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

This would yield the following output which confirms that the function `remove_vowels` behaves as expected for the sample tests provided:
```
''
'bcdf\nghjklm'
'bcdf'
''
'B'
'zbcd'
```

This approach achieves the goal of removing vowels while maintaining the original character positions, and the provided tests comprehensively validate its functionality. Feel free to adapt this solution to your needs. If you have further questions or additional test cases, please don't hesitate to ask!