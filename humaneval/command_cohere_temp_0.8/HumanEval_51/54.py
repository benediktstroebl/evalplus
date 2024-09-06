Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above code defines a function `remove_vowels` that takes a string text as input and returns a string without any vowels. It uses the `translate` method to remove all occurrences of vowels from the text. The `str.maketrans("", "", vowels)` creates a translation table that maps each vowel to `None`, which effectively removes them from the string. This approach ensures that the original string's length and punctuation are maintained, as demonstrated in the provided test cases.