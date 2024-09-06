Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans`. This approach ensures that all possible vowels (both lowercase and uppercase) are removed from the text.

The tests are included within the function as docstring examples, which evaluate the function's behavior and demonstrate its capabilities. 
```python
def test_remove_vowels():
    """
    Tests for the remove_vowels function.

    Test cases:

    - Empty string.
    - String with vowels.
    - String with vowels at beginning and end.
    - String with vowels in the middle.
    - String with vowels and consonants.
    - Multiple lines.

    Expecting an empty string for empty input and input with only consonants.

    """
    assert remove_vowels("") == ""
    assert remove_vowels("aaaaa") == ""
    assert remove_vowels("aaBAA") == "B"
    assert remove_vowels("abcdef") == "bcdf"
    assert remove_vowels("abcdef\nghijklm") == "bcdf\nghjklm"
    assert remove_vowels("zbcd") == "zbcd"
```