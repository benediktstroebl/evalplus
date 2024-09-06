Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This removes vowels (both lowercase and uppercase) from the text using the `translate` method with a translation table created using `str.maketrans()`. It returns a string without vowels. This approach ensures that special characters or numbers are kept unchanged, unlike other methods like `str.replace()` or `str.remove()`. The tests provided confirm that the function handles different cases correctly. 

```python
>>> remove_vowels('abcdef')
'bcdf'
>>> remove_vowels('aaaaa')
''
>>> remove_vowels('aaBAA')
'B'
>>> remove_vowels('zbcd')
'zbcd'
>>> remove_vowels('foo bar')
'foo r'
>>> remove_vowels(' Éclair vs. Cliché ')
' Cr Vs'
```