Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans()`. This approach ensures that all possible vowels, both lowercase and uppercase, are removed from the text.

Here is an example usage of the function:
```python
text = "abcdef"
result = remove_vowels(text)
print(result) # Output: 'bcdf'
```

This code demonstrates how to remove vowels from a given text using the `remove_vowels()` function. It ensures that all types of vowels (lowercase and uppercase) are appropriately excluded, providing a concise and effective solution.