Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    sub_len = len(substring)
    str_len = len(string) 
    i = 0
    while i + sub_len <= str_len:
        if string[i:i+sub_len] == substring:
            count += 1
        i += 1
    return count
```
```python
import unittest

class TestHowManyTimes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_non_empty_string(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_longer_substring(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

if __name__ == '__main__':
    unittest.main()
```

This script includes a test suite with three test functions that check the functionality of the `how_many_times` function. Each test case covers a specific scenario and the `unittest.main()` function runs the test suite when the script is executed directly.