```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This code defines a function called `remove_vowels` that takes one argument, `text`. The function utilizes the `translate` method with custom translations to remove all vowels (both lowercase and uppercase) from the input text and returns the modified text. 

To test this function, you can use the following markdown code block with embedded assertions:
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

The predictions of the behavior of the function are ensured by the tests. They validate that when called with diverse text inputs, the function produces the anticipated results.