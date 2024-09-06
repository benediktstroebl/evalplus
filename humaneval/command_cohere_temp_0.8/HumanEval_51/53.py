Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "AEIOUaeiou"
    return text.translate(str.maketrans("", "", vowels))
```

This removes all vowels (both uppercase and lowercase) from the text using the `translate` method and `str.maketrans` to create a translation table that removes all vowels. It will handle various text scenarios and will return the text without any vowels.