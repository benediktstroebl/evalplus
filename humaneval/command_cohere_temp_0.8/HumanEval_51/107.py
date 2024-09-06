Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above code defines a function called `remove_vowels` that takes a single argument, `text`, which is a string. Inside the function, it defines a string called `vowels` that contains all possible vowels (both lowercase and uppercase). It uses the `translate` method to remove all vowels from the `text` string by creating a translation table using `str.maketrans("", "", vowels)` that removes all vowels. The resulting string is then returned. 
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))

# Test Suite
def test_remove_vowels():
    """
    Test remove_vowels function with various inputs.
    """
    assert remove_vowels("") == ""
    assert remove_vowels("abcdef\nghijklm") == "bcdf\nghjklm"
    assert remove_vowels("abcdef") == "bcdf"
    assert remove_vowels("aaaaa") == ""
    assert remove_vowels("aaBAA") == "B"
    assert remove_vowels("zbcd") == "zbcd"
```
The script also includes a test suite with a `test_remove_vowels` function that tests the `remove_vowels` function with various inputs to verify its correctness.

You can execute this script to run the tests and verify that the `remove_vowels` function meets the specified requirements. 

To solve the problem, the code uses the `translate` method to remove vowels from the text. This approach guarantees that all uppercase and lowercase vowel characters are removed, regardless of the input case. It provides a versatile solution that maintains a consistent result across various test cases.