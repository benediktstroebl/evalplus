Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This removes vowels (both uppercase and lowercase) from the text using the `translate` method with a translation table created using `str.maketrans`. It returns an empty string if the input is empty and does not modify the text if it does not contain any vowels. You can use this code to remove vowels from any string input. 
Let's verify the functionality with some tests:
```python
remove_vowels("")
''
remove_vowels("abcdef\nghijklm")
'bcdf\nghjklm'
remove_vowels('abcdef')
'bcdf'
remove_vowels('aaaaa')
''
remove_vowels('aaBAA')
'B'
remove_vowels('zbcd')
'zbcd'
```

The tests yield the following results, confirming the expected behavior of the `remove_vowels` function.

If you have any more questions or need further assistance, please let me know! I can explain the concepts or provide additional examples if needed.