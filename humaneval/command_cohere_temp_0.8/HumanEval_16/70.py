Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set data structure to remove duplicate characters, regardless of case, and then counts the number of distinct characters in the set.

Here's how you can use it and test it with your provided examples:
```python
import unittest

def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)

class TestCountDistinctCharacters(unittest.TestCase):
    def test_example(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)

    def test_single_character(self):
        self.assertEqual(count_distinct_characters('c'), 1)

if __name__ == '__main__':
    unittest.main()
```
When you run this main.py file, the `TestCountDistinctCharacters` class will execute the test functions, and the output will indicate whether the tests pass. 

This way, you have a self-contained Python module with the function and corresponding tests.  If you have other questions or need further assistance, please let me know!