Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This removes all vowels (both lowercase and uppercase) from the text using the `translate` method and the `maketrans` function. It returns the modified text without vowels.