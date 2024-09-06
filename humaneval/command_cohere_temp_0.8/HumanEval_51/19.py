Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This removes all vowels (both lowercase and uppercase) from the text using the `translate` method with a translation table created using `str.maketrans()`. It leaves other characters untouched. You can test it with the provided tests to ensure it behaves as expected.