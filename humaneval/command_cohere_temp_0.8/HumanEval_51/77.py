```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This code defines a function called `remove_vowels` that takes one argument, `text`. The function utilizes the `translate` method to create a translation table using `str.maketrans("", "", vowels)` that removes all vowels (both lowercase and uppercase) from the text. The translated text is then returned. The `remove_vowels` function effectively removes vowels from the input text and returns the modified string. 

To verify the functionality of the `remove_vowels` function, here is a test drive code:
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

The test drive code provides various scenarios in which the `remove_vowels` function is applied to demonstrate its functionality and verify that it removes vowels from the input text as intended.