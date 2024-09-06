```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This code defines a function called `remove_vowels` that takes one argument, `text`. It creates a translation table using `str.maketrans("", "", vowels)` that maps each vowel (both lowercase and uppercase) to `None`. It then uses the `translate()` method to apply this translation to the input text, removing all vowels. The function returns the modified text without vowels. 

To follow the specification in the problem statement, the code includes a markdown block with example tests and the expected output.
```python
```python
def test_remove_vowels():
    assert remove_vowels("") == ""
    assert remove_vowels("abcdef\nghijklm") == "bcdf\nghjklm"
    assert remove_vowels("abcdef") == "bcdf"
    assert remove_vowels("aaaaa") == ""
    assert remove_vowels("aaBAA") == "B"
    assert remove_vowels("zbcd") == "zbcd"
```

This block includes specific test cases that cover different scenarios and ensure the function's correctness and its behaviour corresponds to the problem statement.

The code is organised using the `remove_vowels()` function to encapsulate the logic, making it reusable and easy to understand. The `test_remove_vowels()` function provides robust test coverage to verify the function's behaviour.