Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "AEIOUaeiou"
    return text.translate(str.maketrans("", "", vowels))
```
The above code defines a function `remove_vowels` that takes a string text as an argument and returns a string without any vowels. It uses the `translate` method to remove all occurrences of vowels from the text. The `str.maketrans("", "", vowels)` creates a translation table that maps each vowel to `None`, which means those characters will be removed from the text.

Here's the markdown code block with the Python script to solve the problem:
```python
def remove_vowels(text):
    vowels = "AEIOUaeiou"
    return text.translate(str.maketrans("", "", vowels))

``````