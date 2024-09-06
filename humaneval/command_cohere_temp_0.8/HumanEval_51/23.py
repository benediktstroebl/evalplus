Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels (both uppercase and lowercase) from the input text using the `translate` method with a translation table created using `str.maketrans()`. This approach ensures that all occurrences of vowels are removed while maintaining the relative positions of non-vowel characters. The tests provided for the function demonstrate its behavior and show that it passes all the given test cases.

Here's an explanation of the solution:
1. The `def remove_vowels(text):` statement defines a function named `remove_vowels` that takes a single argument called `text`.
2. The `vowels` variable is defined as a string containing all lowercase and uppercase vowel characters. This variable will be used to create the translation table.
3. The `return text.translate(str.maketrans("", "", vowels))` line uses the `translate()` method to remove vowels from the input `text`. The `str.maketrans("", "", vowels)` creates a translation table that maps each character in `vowels` to `None`, effectively removing them from the string.

By using this approach, the function seamlessly handles various cases, including empty strings, strings with and without line breaks, and cases where the vowels constitute a significant portion of the string. The function's behavior aligns with the problem's requirement of removing vowels while preserving the positions of non-vowel characters.