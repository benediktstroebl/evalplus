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

    def test_multiple_occurrences(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_overlapping_occurrences(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('aaa', 'b'), 0)

if __name__ == '__main__':
    unittest.main()
```
This script includes a test suite with four distinct test cases to ensure the `how_many_times` function operates correctly. Each test case concentrates on a specific scenario, guaranteeing that the function returns the anticipated results.

When you execute this script, the `unittest` module will run the test suite, and the results will be displayed. If all test cases pass, you will get an output that indicates the number of tests executed and the number of failures or errors. However, if any test case fails, the place in the script where the unexpected behavior occurs will be indicated. 

This way, you can independently verify that the function works appropriately in different contexts. You can copy this code and run it in your Python environment to see the results directly or modify the code as per your specific requirements.