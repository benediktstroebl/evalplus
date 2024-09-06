Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels (both uppercase and lowercase) from a given text using the `translate` method with a translation table created using `str.maketrans`. It supports various edge cases like empty strings, strings with newlines, and cases where removing vowels results in an empty string.

Here's the code with the additional test cases to verify its behavior:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))

def test_remove_vowels():
    cases = [
        ("", ""),
        ("abcdef\nghijklm", "bcdf\nghjklm"),
        ("abcdef", "bcdf"),
        ("aaaaa", ""),
        ("aaBAA", "B"),
        ("zbcd", "zbcd"),
    ]

    for input_, output in cases:
        assert remove_vowels(input_) == output

if __name__ == "__main__":
    test_remove_vowels()
```

When you run this script, you can observe that all test cases get passed, confirming the correct removal of vowels from different scenarios.