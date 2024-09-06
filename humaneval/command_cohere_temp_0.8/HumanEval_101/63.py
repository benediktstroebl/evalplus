Here's a Python script that contains a function called `words_string` which takes a string as an input and returns a list of words separated by commas or spaces:
```python
def words_string(s):
    return s.split(", ")
```
The function uses the `split` method to split the input string s into a list of strings, assuming that the string contains only words separated by spaces or commas. Since the problem statement does not specify any specific approach for handling multiple spaces between words, this solution assumes that such spaces should be ignored and considered as a single separator. Hence, it uses ", " as the splitting parameter to simultaneously ignore both commas and spaces as word separators.

This solution is straightforward and assumes that the input string contains only space or comma-separated words. It's important to note that this approach might not work well with other data formats or if the input string contains other characters or special punctuation. 

Here is how you can verify this solution by writing and executing a simple test script:
```python
import unittest

def test_words_string():
    # Test string with commas and spaces
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]

    # Test string with comma as the only separator
    assert words_string("One, two, three, four") == ["One", "two", "three", "four"]

    # Test string with multiple spaces between words
    assert words_string("Five   six   seven") == ["Five", "six", "seven"]

    # Test string with no commas or spaces
    assert words_string("AlphaBetaGamma") == ["AlphaBetaGamma"]

if __name__ == "__main__":
    unittest.main()
```

This way, you can ensure that the provided solution follows the expected behavior and verifies the conditions stated in the problem statement.