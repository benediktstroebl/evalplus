Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans()`. The result is returned as the modified text. The `tests` module checks if the function works correctly for different cases. 

```python
tests = {
    ("", ""),
    ("abcdef\nghijklm", "bcdf\nghjklm"),
    ("abcdef", "bcdf"),
    ("aaaaa", ""),
    ("aaBAA", "B"),
    ("zbcd", "zbcd"),
}

for inp, out in tests:
    assert remove_vowels(inp) == out
```

The tests input, expected output, and the actual output are strings that are compared using the `assert` statement.