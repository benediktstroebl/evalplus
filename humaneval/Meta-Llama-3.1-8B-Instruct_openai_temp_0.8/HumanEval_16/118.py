```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    Args:
        string (str): The input string.
    
    Returns:
        int: The number of distinct characters in the string.
    """
    return len(set(string.lower()))

# Test cases
import unittest

class TestCountDistinctCharacters(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
    
    def test_case2(self):
        self.assertEqual(count_distinct_characters('Jerry'), 4)
    
    def test_case3(self):
        self.assertEqual(count_distinct_characters('AABBCC'), 3)

if __name__ == '__main__':
    unittest.main()
```

This script defines a function `count_distinct_characters` that takes a string as input, converts it to lowercase using the `lower()` method, and then uses a set to count the distinct characters. The `set` data structure in Python is a collection of unique elements, so the number of elements in the set is the number of distinct characters in the string. The `len()` function is used to get the number of elements in the set.

The script also includes test cases using the `unittest` module to ensure the function works correctly.