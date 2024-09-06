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

    def test_multiple_overlapping_substring(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('aaaa', 'b'), 0)

if __name__ == '__main__':
    unittest.main()
```

This script includes a test suite with different test cases to validate the behavior of the `how_many_times` function. You can execute the script to run the tests or adapt it to your needs.  If you need help understanding any of the functions, let me know.