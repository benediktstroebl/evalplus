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

    def test_single_char(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_2_chars(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_multiple_occurrences(self):
        self.assertEqual(how_many_times('ababab', 'ab'), 5)

if __name__ == '__main__':
    unittest.main()
```

This script includes a test suite with a variety of cases to ensure the `how_many_times` function behaves as expected. You can run the script to execute the tests or use a IDE to run the test suite individually.  The function `how_many_times` takes two strings as input and returns the number of times the second string (substring) appears in the first string (string), including overlapping occurrences.