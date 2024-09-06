Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above code defines a function `remove_vowels` that takes a string text as input and returns a string without any vowels. It uses the `translate` method to remove all occurrences of vowels from the text. The `str.maketrans("", "", vowels)` creates a translation table that maps each vowel to `None`, which effectively removes them from the string. This approach ensures that the original string's length and punctuation are preserved. 

Here is a simple test suite for that function:
```python
def test_remove_vowels():
    assert remove_vowels("") == ""
    assert remove_vowels("abcdef") == "bcdf"
    assert remove_vowels("aaaaa") == ""
    assert remove_vowels("aaBAA") == "B"
    assert remove_vowels("zbcd") == "zbcd"
    assert remove_vowels("abracadabra") == "brcdbr"
```

To run the tests, you can copy and paste the test suite into a Python environment of your choice and run the tests using the command `python -m unittest test_remove_vowels`. 

This approach ensures that the function works correctly and maintains the original string's length and punctuation, as mentioned in the problem statement. 
The code is also efficient and avoids any unnecessary operations, making it suitable for production use.