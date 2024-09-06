Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels (both uppercase and lowercase) from a given text using the `translate` method with a translation table created using `str.maketrans`. This approach ensures that all occurrences of vowels are removed from the text without modifying other characters. The unit tests demonstrate the correct behavior of the function for various input scenarios.

```python
def test_remove_vowels():
    assert remove_vowels("") == ""
    assert remove_vowels("abcdef\nghijklm") == "bcdf\nghjklm"
    assert remove_vowels("abcdef") == "bcdf"
    assert remove_vowels("aaaaa") == ""
    assert remove_vowels("aaBAA") == "B"
    assert remove_vowels("zbcd") == "zbcd"

test_remove_vowels()
```

Feel free to modify the tests or add additional cases to ensure the function's behavior matches your problem statement perfectly. Let me know if you have any further questions or need help with anything else!