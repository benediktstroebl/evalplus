Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above code defines a function `remove_vowels` that takes a string as an argument and returns a string without any vowels. It uses the `translate` method to remove all occurrences of vowels (both lowercase and uppercase) from the text. The `str.maketrans("", "", vowels)` creates a translation table that maps every vowel to `None`, effectively removing them from the string. This approach ensures that the original string's length and punctuation are maintained, and it can handle various cases, including empty strings, multiline strings, and cases with different letter cases.