Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above code defines a function `remove_vowels` that takes a string text as an input and returns a string without any vowels. It uses the `translate` method to remove vowels from the text using a translation table created with `str.maketrans("", "", vowels)` where `vowels` is a string containing all lowercase and uppercase vowels.

Here is an example usage of this function:
```python
remove_vowels("abcdef")
```
This would return the string `bcdf` because the vowels in the string `abcdef` are removed.