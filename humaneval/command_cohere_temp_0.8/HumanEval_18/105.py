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

    def test_empty(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_match(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_double_match(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_non_matching(self):
        self.assertEqual(how_many_times('aaaa', 'bb'), 0)

if __name__ == '__main__':
    unittest.main()
```

This script includes a test suite with four individual test functions that verify the behavior of the `how_many_times` function for different cases. Each test case validates a specific condition and asserts that the function returns the expected result. Running the test suite ensures that the function operates correctly in different scenarios and helps maintain the code's integrity. 

The `how_many_times` function counts overlapping occurrences of the `substring` within the `string`. It iterates through non-overlapping windows of the `string` of length equal to the length of the `substring`, and counts the instances where the `substring` aligns perfectly within these windows. The function returns the total count of such occurrences. 

----

If you have any more questions or need assistance with anything else, please let me know! I'm here to help.