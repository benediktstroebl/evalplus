Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans`. This approach ensures that all types of vowels (lowercase, uppercase, and title case) are removed correctly. The tests provided in the original prompt are included and adjusted to fit the expected output.

```python
remove_vowels("abcdef") == "bcdf"
remove_vowels("aaaaa") == ""
remove_vowels("aaBAA") == "B"
remove_vowels("zbcd") == "zbcd"
remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'
```