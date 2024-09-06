```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```

This approach utilizes the `re.findall` method to find all substrings consisting of one or more alphanumeric characters (letters or digits), which effectively captures individual words within the given string. The regular expression pattern `\w+` matches one or more word characters, which include letters, digits, and underscores.

To apply this code, you can use it as follows:
```python
import unittest

class TestWordsString(unittest.TestCase):
    def test_hi_my_name_is_john(self):
        self.assertEqual(words_string("Hi, my name is John"), ["Hi", "my", "name", "is", "John"])

    def test_one_two_three_four_five_six(self):
        self.assertEqual(words_string("One, two, three, four, five, six"), ["One", "two", "three", "four", "five", "six"])

    def test_empty_string(self):
        self.assertEqual(words_string(""), [])

    def test_string_with_single_word(self):
        self.assertEqual(words_string("Hello"), ["Hello"])

    def test_string_with_punctuation(self):
        self.assertEqual(words_string("One, two! Three? Four"), ["One", "two", "Three", "Four"])

if __name__ == '__main__':
    unittest.main()
```

This driver code provides a `unittest` powered test suite with various test cases to cover different scenarios. It asserts that the `words_string` function produces the expected outputs for each scenario, ensuring the accuracy of the function in splitting words from the given string.