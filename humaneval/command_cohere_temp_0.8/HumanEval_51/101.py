Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans()`. The empty string argument passed to `str.maketrans()` creates a mapping that removes all vowels from the text.

To execute this code and verify its behavior against the provided tests, create a Python file, e.g., `remove_vowels.py`, and copy this script into it. Then, run the file with:
```bash
$ python remove_vowels.py
```

The tests will be executed, and the output will confirm the expected behavior of the `remove_vowels` function.

```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))

def test_remove_vowels():
    assert remove_vowels("") == ""
    assert remove_vowels("abcdef\nghijklm") == "bcdf\nghjklm"
    assert remove_vowels("abcdef") == "bcdf"
    assert remove_vowels("aaaaa") == ""
    assert remove_vowels("aaBAA") == "B"
    assert remove_vowels("zbcd") == "zbcd"

test_remove_vowels()
```

The test cases cover different scenarios, including empty strings, different types of vowels, and different text structures. The final assertion verifies that the function behaves as expected for the provided test cases.