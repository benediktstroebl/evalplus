```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This code defines a function called `remove_vowels` that takes one argument, `text`. The function utilizes the `translate` method with custom translation tables to remove all vowels (both lowercase and uppercase) from the input text and returns the modified text. 

To demonstrate the function's behavior, here is an example:
```python
>>> remove_vowels("abcdef")
'bcdf'
>>> remove_vowels("aaaaa")
''
>>> remove_vowels("aaBAA")
'B'
>>> remove_vowels("zbcd")
'zbcd'
```

The expected outcome is to have the vowels removed from the text, and the examples showcase how the function achieves this.