Here is a Python script that contains a self-contained function to count the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a string, regardless of case.
    Args: 
    - string (str) -- input string

    Returns: 
    - int -- number of distinct characters
    """
    return len([char for char in string.isupper(char)]) + len([char for char in string if not char.isalpha()]

# Unit tests
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4
```
This code defines a function `count_distinct_characters` that calculates the number of unique characters in a given string. It returns an integer count of distinct characters. The function also includes unit tests to ensure its correctness.