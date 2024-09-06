Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above code defines a function `remove_vowels` that takes a string `text` as an input and returns a string without any vowels. The function uses the `translate` method to remove vowels. The `str.maketrans("", "", vowels)` creates a translation table that maps each character in `vowels` to `None`, which means those characters will be removed from the string. 

Here is a simple test suite for that function:
```python
def test_remove_vowels():
    assert remove_vowels("") == ""
    assert remove_vowels("abcdef") == "bcdf"
    assert remove_vowels("aaaaa") == ""
    assert remove_vowels("aaBAA") == "B"
    assert remove_vowels("zbcd") == "zbcd"
    assert remove_vowels("abcdef\nghijklm") == "bcdf\nghjklm"
```

You can test the function by calling it with different inputs to verify its behavior. You can also add more test cases to cover a wide range of scenarios and corner cases.