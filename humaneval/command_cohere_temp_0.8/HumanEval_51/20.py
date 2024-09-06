Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans`. It supports various edge cases like handling empty strings, handling input with newlines, and preserving non-vowel characters.

Here's a markdown code block with the Python script:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This approach ensures that the output contains only the non-vowel characters from the input text, regardless of the characters present.