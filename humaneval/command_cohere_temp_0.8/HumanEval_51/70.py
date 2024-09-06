Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This removes all vowels (both lowercase and uppercase) from the text using the `translate` method with a translation table created using `str.maketrans`. It leaves the punctuation and other characters untouched. Here is an example:
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

The tests match the prompt's expectations and demonstrate the function's behavior. 
If you have additional test cases or require further clarification, feel free to ask! 
If you'd like to cover aspects related to edge cases, efficiency, or other concerns, please provide additional test scenarios. 
Feel free to modify the tests according to your needs.