Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans`. It supports various edge cases like empty strings, different text lengths, and cases where vowels are present in different positions. The tests confirm that the function behaves as expected in each case.

The test cases are defined as follows:
```python
def test_remove_vowels():
    assert remove_vowels("") == ""
    assert remove_vowels("abcdef\nghijklm") == "bcdf\nghjklm"
    assert remove_vowels("abcdef") == "bcdf"
    assert remove_vowels("aaaaa") == ""
    assert remove_vowels("aaBAA") == "B"
    assert remove_vowels("zbcd") == "zbcd"
```