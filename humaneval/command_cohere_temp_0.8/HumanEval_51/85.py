Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This script defines a function called `remove_vowels` that takes a string as an input and returns a string without any vowels. It uses the `translate` method to remove all occurrences of vowels from the input string. The `str.maketrans("", "", vowels)` creates a translation table that maps each vowel to `None`, which effectively removes them from the string.

Here is an example usage of this function:
```python
remove_vowels("abcdef")
```

The output of this code will be:
```
bcdf
```

This function performs the task of removing vowels from a given string effectively and efficiently.