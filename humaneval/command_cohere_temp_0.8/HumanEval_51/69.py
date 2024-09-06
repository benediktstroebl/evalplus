Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans`. This approach ensures that all possible vowels, both lowercase and uppercase, are removed from the text. The tests provided in the problem statement are covered by the provided test cases, demonstrating the function's ability to handle different scenarios.

Here is an example usage of the function:
```python
remove_vowels("abcdef")
# 'bcdf'
```

This would return "bcdf" as expected, indicating the removal of all vowel characters from the input string.