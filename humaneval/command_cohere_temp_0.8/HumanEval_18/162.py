Here's a Python script that contains a function called `how_many_times` that solves the problem you've described:
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

This function takes two strings as input: the `string` and the `substring`. It returns an integer value indicating how many times the `substring` appears in the `string`, including overlapping instances. 

To validate the functionality of this function, let's run some test cases using Python's built-in `unittest` module:
```python
import unittest

class HowManyTimesTest(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('aaa', 'b'), 0)

    def test_equal_strings(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_overlapping_instances(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

if __name__ == '__main__':
    unittest.main()
```

This test suite covers various scenarios, including handling empty strings, checking if a substring is not found, verifying identical strings, and testing for overlapping instances.

To run these tests, simply execute the Python script. You can use an IDE or the command line to run the file containing the test cases. The `unittest` framework will then execute each test and report any failures or errors, ensuring the `how_many_times` function operates as expected.