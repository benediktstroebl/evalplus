```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This code defines a function called `remove_vowels` that takes one argument, `text`. The function uses the `translate` method to create a translation table using `str.maketrans("", "", vowels)` where `vowels` is a string containing all lowercase and uppercase vowels. This translation table is used to remove all vowels (both lowercase and uppercase) from the `text` argument. The function then returns the modified string.

The behavior of the function is demonstrated through examples in the accompanying docstring, which also includes tests that check whether the function behaves as expected. These tests ensure that the function handles empty strings, multiline inputs, and cases where the input string contains only vowels or only vowels and consonants.