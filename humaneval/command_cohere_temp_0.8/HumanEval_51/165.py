```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This removes all vowels (both uppercase and lowercase) from a given text. It uses the `translate` method with a translation table created using `str.maketrans` to remove all instances of vowels from the text.