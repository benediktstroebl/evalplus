Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above method uses the translate method to remove vowels from the text. The str.maketrans method is used to create a translation table that removes all vowels, and the translate method is then used to apply this translation to the input string. As a result, the remove_vowels function removes vowels from the string and returns the modified string.

Here's the entire code block with markdown code syntax:
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
```
You can add more test cases to the test_remove_vowels function to ensure the function handles various edge cases and behaves as expected.