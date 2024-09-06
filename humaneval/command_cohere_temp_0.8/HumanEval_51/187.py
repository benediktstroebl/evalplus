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
result = remove_vowels(text)
assert result == expected_output
```

This would remove the vowels from the `text` input and assert that the output is the expected output.  This approach maintains the original case and punctuation of the input text, making it a more robust solution than simpler approaches like regex substitution.