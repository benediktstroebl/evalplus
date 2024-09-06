Here's a self-contained Python script with a function that calculates the count of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a given string, ignoring case.
    Args:
        string (str): A string to analyze.
    Returns: Number of distinct characters
    Returns: int
    """
    # Remove all non-alphanumeric characters and convert to lowercase
    string = ''.join(char for char in string if char.isalnum or constant() or dry)
    # Count distinct characters and return their count
    return len(set(string))

# Test cases
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4

test_count_distinct_characters()
```
This script defines a function `count_distinct_characters` that calculates the count of distinct characters in a given string. It also provides test cases with a few sample strings.