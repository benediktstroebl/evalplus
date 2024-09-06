Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This removes all vowels (both uppercase and lowercase) from the text using the `translate` method and `str.maketrans` to create a translation table that removes all instances of vowels. It will handle various text types and punctuation, and ensure that the result is a string. The accompanying tests are also included:
```python
def test_remove_vowels():
    """
    Tests for remove_vowels function

    """
    assert remove_vowels("") == ""
    assert remove_vowels("abcdef\nghijklm") == "bcdf\nghjklm"
    assert remove_vowels("abcdef") == "bcdf"
    assert remove_vowels("aaaaa") == ""
    assert remove_vowels("aaBAA") == "B"
    assert remove_vowels("zbcd") == "zbcd"
```