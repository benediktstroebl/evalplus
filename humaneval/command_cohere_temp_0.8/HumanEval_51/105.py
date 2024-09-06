Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above code defines a function `remove_vowels` that takes a string text as input and returns a string without any vowels. It uses the `translate` method to remove all occurrences of vowels (both lowercase and uppercase) from the input text. The `maketrans` function is used to create a translation table that maps each vowel to `None`, effectively removing them from the string. This approach ensures that only vowels are removed, and other characters remain unchanged.