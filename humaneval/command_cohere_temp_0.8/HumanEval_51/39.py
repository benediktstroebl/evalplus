Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans`. This approach ensures that all possible vowels, both lowercase and uppercase, are removed from the text. The tests provided in the problem statement demonstrate the correct behavior of the function.

Here's an example of how you can use this function in your code:
```python
result = remove_vowels("Hello, World!")
print(result)  # Output: "Hll, Wrd!"
```

This demonstrates how the `remove_vowels` function can be used effectively to remove vowels from any string.