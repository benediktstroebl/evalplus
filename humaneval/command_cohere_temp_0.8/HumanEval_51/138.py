Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans`. It supports various test cases including empty strings, different text lengths, and cases where vowels are present in different positions. The expected behavior of the function is to return the modified text without vowels. Feel free to test it with other scenarios as needed!