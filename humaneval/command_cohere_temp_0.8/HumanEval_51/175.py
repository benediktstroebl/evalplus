Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans`. This approach ensures that all types of vowels (lowercase and uppercase) are removed correctly. The tests demonstrate the correct behavior of the function against various input scenarios.

```python
remove_vowels("abcdef")  # Output: 'bcdf'
remove_vowels("aaaaa")  # Output: ''
remove_vowels("aaBAA")  # Output: 'B'
remove_vowels("zbcd")  # Output: 'zbcd'
```