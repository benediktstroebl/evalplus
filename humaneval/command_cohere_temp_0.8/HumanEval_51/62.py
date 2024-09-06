Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This function removes vowels (both uppercase and lowercase) from the input text using the `translate` method with a translation table created using `str.maketrans()`. The empty string "" passed as the second argument to `str.maketrans()` ensures that the translation leaves other characters unchanged. The result is returned as the modified text without vowels.