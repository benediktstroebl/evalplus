Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels (both lowercase and uppercase) from the input text using the `translate` method with a translation table created using `str.maketrans()`. This approach ensures that all occurrences of vowels are removed while retaining non-vowel characters. The expected behavior is for the function to return the modified text without vowels.

This approach is also efficient and suitable for processing large inputs, making it practical for various real-world scenarios.