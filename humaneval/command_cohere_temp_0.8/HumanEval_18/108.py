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

    def test_overlapping_matches(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('aaaa', 'b'), 0)

    def test_empty_substring(self):
        self.assertEqual(how_many_times('aaaa', ''), 0)

if __name__ == '__main__':
    unittest.main()
```
This script includes a test suite with a variety of tests to validate the behavior of the `how_many_times` function. You can execute the script to run the tests or edit the function to see if the tests pass.  This will ensure that the function operates correctly and aligns with the problem statement. 
The function `how_many_times` accepts a string `string` and a substring `substring` as inputs and returns the number of times the substring occurs within the string, even if the instances overlap.