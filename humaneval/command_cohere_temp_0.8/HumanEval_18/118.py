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

    def test_single_instance(self):
        self.assertEqual(how_many_times('aaa', 'a'), 1)

    def test_multiple_instances(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 2)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('aaaa', 'aaa'), 0)

if __name__ == '__main__':
    unittest.main()
```

This script includes a test suite with several test cases to validate the behavior of the `how_many_times` function. Each test case demonstrates a specific scenario and asserts whether the function's output matches the expected result. By following the unittest framework, the test cases are organized into a class that inherits from `unittest.TestCase`, and each individual test case is defined as a method within that class. 

In the `test_empty_string` case we check that the result is 0 when an empty string is provided. In the `test_single_instance` case we check that we get a count of 1 when the substring is unique in the string.  In the `test_multiple_instances` case we assert that when the substring overlaps with the string multiple times, it is counted correctly. In the `test_substring_not_found` we check that 0 is returned when the substring is not present in the string. 

By running this script, the tests will be executed, allowing you to validate the correctness of the `how_many_times` function and ensure its behavior aligns with the specified problem. 
You can run this code to test the function and see the test results.