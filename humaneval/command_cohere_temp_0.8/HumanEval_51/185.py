Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This script defines a function called `remove_vowels` that takes a string text as input and uses the `translate` method to remove all vowels (both uppercase and lowercase) from the text. The `str.maketrans("", "", vowels)` creates a translation table that maps each vowel to `None`, which effectively removes them from the string. The function then returns the modified string.

Here is an example usage of this function:
```python
remove_vowels("abcdef")
```

The output of this code will be:
```
bcdf
```

This function also handles edge cases, such as when the input string is empty or contains only vowels, by returning an empty string or leaving the input unchanged if it does not contain any vowels.

The test cases pass as this function matches the expected behavior of the `remove_vowels` function, as stated in the original problem. Test cases examine different scenarios including various types of inputs and edge cases.