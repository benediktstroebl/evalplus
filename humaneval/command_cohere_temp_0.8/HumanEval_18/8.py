Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    sub_len = len(substring)
    for i in range(len(string) - sub_len + 1):
        if string[i:i+sub_len] == substring:
            count += 1
    return count
```
```python
import unittest

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_char_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_overlapping_cases(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_subsequent_occurrences(self):
        self.assertEqual(how_many_times('car car car', 'car'), 3)

if __name__ == '__main__':
    unittest.main()
```

This script includes a test suite with a variety of test cases to validate the behavior of the `how_many_times` function. Each test case demonstrates a specific scenario and the expected outcome. By executing the `unittest` module, all the tests will be run, and the script will provide test results, including failure details if any problems are encountered.

Make sure to install the required dependencies (`unittest` is included in the standard library, so no installation is required for it) for the code to run successfully.

Let me know if you need any further clarification or additional details!