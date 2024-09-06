Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans`. This approach ensures that all possible vowels, both lowercase and uppercase, are removed from the text.

Here's an example usage of the function:
```python
result = remove_vowels("Hello, World!")
print(result)
```

Output:
```
Hll, Wrd!
```

This demonstrates how the `remove_vowels` function effectively removes vowels from the input text, regardless of their case.