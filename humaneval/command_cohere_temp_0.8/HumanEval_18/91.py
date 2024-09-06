Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    substring_length = len(substring)
    string_length = len(string)
    for i in range(string_length - substring_length + 1):
        if string[i:i + substring_length] == substring:
            count += 1
    return count
```
```python
import unittest

class HowManyTimesTest(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_occurrence(self):
        self.assertEqual(how_many_times('aaa', 'a'), 1)

    def test_multiple_occurrences(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 2)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('aaaa', 'bb'), 0)

if __name__ == '__main__':
    unittest.main()
```

This script includes a test suite with four individual test functions that verify the behavior of the `how_many_times` function for different cases. Each test case asserts that the function returns the expected output based on the provided inputs.

Note: The `how_many_times` function performs an inefficient linear search while counting overlapping occurrences of the substring. For scalability, a more efficient approach could be contemplating employing techniques like rolling hash to tally occurrences of a substring in a string. This approach significantly improves efficiency by decreasing the number of comparisons required.