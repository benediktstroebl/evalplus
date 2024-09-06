Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the string after converting all characters to lowercase. This ensures that characters like 'x' and 'X' are treated as the same character. Finally, it returns the length of the set, which is the number of distinct characters.

To execute this function, you can simply import the required Python standard library `unittest` module and use the `@unittest.jupiter` decorator to define test cases. Here's a minimal test suite with two test cases that cover positive and edge cases:
```python
import unittest

def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)

class TestCountDistinctCharacters(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)

    def test_edge_case(self):
        self.assertEqual(count_distinct_characters('Jerry'), 4)
```
You can run this test suite using any Python test runner, such as the built-in `unittest` module runner, to verify the correctness of the `count_distinct_characters` function.