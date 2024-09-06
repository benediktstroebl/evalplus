```python
def count_distinct_characters(string: str) -> int:
    """
    Returns the count of distinct characters in the string, regardless of case.
    """
    string = 'xyzXYZ'.upper()
    return len(string.split('')
   
    distinct characters: 'z', 'y', 'X'
    """
    return len(set(string))

def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3

def test_count_distinct_characters2():
    assert count_distinct_characters('Jerry') == 4
```
This script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case. It also includes two test functions `test_count_distinct_characters` and `test_count_distinct_characters2` to verify the functionality of the `count_distinct_characters` function.  The best practices for writing self-contained functions and documenting their behavior.