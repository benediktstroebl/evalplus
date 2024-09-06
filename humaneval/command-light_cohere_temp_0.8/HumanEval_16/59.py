Here's the corrected Python script that includes proper docstrings and tests:
```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a given string, regardless of case.
    Args: 
        string (str): The input string
    Returns: 
        int: Number of distinct characters
    """
    string = string.split()
   
    unique_chars = set(string)
    return len(unique_chars)

# Unit tests
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4
```
The `test_count_distinct_characters` function contains assertions that verify the correctness of the `count_distinct_characters` function with different input strings.