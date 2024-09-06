Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans`. It supports various test cases including empty strings, different text cases, and different types of input texts.

Here's an example of how to use the function:
```python
print(remove_vowels("abcdef"))  # Outputs: 'bcdf'
print(remove_vowels("aaaaa"))  # Outputs: ''
print(remove_vowels("aaBAA"))  # Outputs: 'B'
print(remove_vowels("zbcd"))  # Outputs: 'zbcd'
```

The expected output of each example is demonstrated above. The function removes vowels depending on the given text and its state (lowercase or uppercase) and returns the modified text.