Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the string after converting all characters to lowercase. This ensures that both 'x', 'X', and 'x1' are considered the same character. Finally, it returns the count of distinct characters in the set. 

The tests mentioned earlier can be done on this function by using Python's built-in `unittest` module. Here's how the test would look:
```python
import unittest

def test_count_distinct_characters():
    # Test case one
    assert count_distinct_characters('xyzXYZ') == 3
    
    # Test case two
    assert count_distinct_characters('Jerry') == 4
    
if __name__ == '__main__':
    unittest.main()
```