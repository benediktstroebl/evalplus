Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans`. This approach ensures that all possible vowels, both lowercase and uppercase, are removed from the text.

Here is an example usage of the function:
```python
text = "abcdef"
expected_output = "bcdf"
output = remove_vowels(text)

assert output == expected_output
```

The test case demonstrates how to call the `remove_vowels` function with the `abcdef` input and verify that the output is `bcdf`, matching the updated problem statement.

The script ensures that leading and trailing blanks are correctly handled, while preserving non-vowel characters and punctuation. It also supports multi-line inputs, providing a comprehensive solution for removing vowels from strings in various scenarios.