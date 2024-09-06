Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This removes vowels from the text using the `translate` method with a translation table created using `str.maketrans`. It supports various test cases including empty strings, different text cases, and different types of input texts.

The script can be explained as follows:
1. The `def remove_vowels(text)` function definition declares a function named `remove_vowels` that takes a single argument called `text`.
2. The `vowels` variable is assigned the string value `'aeiouAEIOU'`, which contains all lowercase and uppercase vowel characters.
3. The `return text.translate(str.maketrans("", "", vowels))` line uses the `translate` method to remove vowels from the `text` string. The `str.maketrans("", "", vowels)` creates a translation table that maps each character in `vowels` to `None`, effectively removing them from the string.

The resulting `remove_vowels` function is a self-contained solution to the problem, and it can be used in other Python scripts to remove vowels from any given string.