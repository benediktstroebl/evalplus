Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    sub_len = len(substring)
    str_len = len(string)
    for i in range(str_len - sub_len + 1):
        if string[i:i+sub_len] == substring:
            count += 1
    return count
```
```python
import unittest

class TestHowManyTimes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_overlapping_cases(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_subsequent_occurrences(self):
        self.assertEqual(how_many_times('ccaacacc', 'aa'), 2)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('aaa', 'b'), 0)

if __name__ == '__main__':
    unittest.main()
```

This script includes a test suite with a variety of test cases to validate the behavior of the `how_many_times` function. It checks for edge cases like empty strings, single characters, overlapping occurrences, and non-existent substrings. The `unittest.main()` function is used to discover and run the tests.