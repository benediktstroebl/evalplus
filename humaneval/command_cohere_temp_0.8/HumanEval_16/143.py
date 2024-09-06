Here's a Python script that contains a function to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The function `count_distinct_characters` takes a string as an argument and returns the number of distinct characters within the string, regardless of case. The function uses a set data structure to remove duplicate characters and ensure that only distinct characters are counted.

To test this function, let's use Python's built-in `unittest` framework. Create a test module named `test_count_distinct_characters.py` and place the following content in it:
```python
import unittest
from count_distinct_characters import count_distinct_characters

class TestDistinctCharacters(unittest.TestCase):
    def test_distinct_characters(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
    def test_distinct_mixed_case_characters(self):
        self.assertEqual(count_distinct_characters('Jerry'), 4)
    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)
    def test_only_whitespace(self):
        self.assertEqual(count_distinct_characters('       '), 0)
if __name__ == '__main__':
    unittest.main()
```

The test module will ensure that the `count_distinct_characters` function behaves as expected and will provide feedback in the event of errors or incorrect assumptions. To run the tests, navigate to the directory containing the `test_count_distinct_characters.py` file and execute the command `python test_count_distinct_characters.py`. 

In the command line, you will see the progress of the test execution, showcasing the number of passed tests along with any failures or errors encountered within the test suite.