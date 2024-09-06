Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans`. This approach ensures that all possible vowels, both lowercase and uppercase, are removed from the text. The tests provided for the function demonstrate its correctness and versatility in handling various scenarios.

Here is an example of how to use this function:
```python
remove_vowels("Hello, World!")
# 'Hll, Wrd!'
```