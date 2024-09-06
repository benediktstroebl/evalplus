Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans()`. The process builds a translation table that removes all vowels, empties the translation table, and then applies it to the original text. The function returns the modified text without vowels. 

This solution is efficient and provides a clear separation between the problem statement and the code solution. It removes vowels without creating unnecessary new strings or causing unnecessary memory usage, improving overall efficiency and readability.