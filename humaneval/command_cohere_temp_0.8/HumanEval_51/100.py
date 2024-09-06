Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans`. It supports various edge cases like handling empty strings, multiple lines, and maintaining non-vowel characters.

Here's a test suite to verify the function:
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

Running the test suite ensures that the `remove_vowels` function behaves as expected. 

This approach guarantees that the function performs as designed while maintaining compatibility with Python 3.9 and higher. Additionally, it adheres to the problem's requirement of a self-contained solution within a single Python script.