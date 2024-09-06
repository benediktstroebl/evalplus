Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    substring_length = len(substring)
    string_length = len(string)
    for i in range(string_length - substring_length + 1):
        if string[i:i+substring_length] == substring:
            count += 1
    return count
```
```python
import unittest

class HowManyTimesTest(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_multiple_occurrences(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_overlapping_occurrences(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_different_string(self):
        self.assertEqual(how_many_times('123', '32'), 1)

if __name__ == '__main__':
    unittest.main()
```
This script includes a test suite with a variety of test cases to validate the behavior of the `how_many_times` function. Each test case asserts that the result of the function corresponds to the expected number of occurrences of the substring in the string. 

You can execute this script to run the tests and verify that the function behaves as expected. Let me know if you have any questions or if you'd like to further refine the solution.