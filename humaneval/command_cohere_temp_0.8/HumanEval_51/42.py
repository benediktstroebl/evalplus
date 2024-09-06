Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels (both uppercase and lowercase) from a given text using the `translate` method with a translation table created using `str.maketrans`. It returns the modified text without vowels.