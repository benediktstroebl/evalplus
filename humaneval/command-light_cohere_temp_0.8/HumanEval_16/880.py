```python
def count_distinct_characters(string):
    """ Returns the number of distinct characters in the given string (case-insensitive).
    Args:
        string (str): input string
    Returns:
        int: number of distinct characters
    """
    string = string.split()
    distinct = set()
    return len(distinct)

# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('abcX') == 3
assert count_distinct_characters('JERRY') == 4
assert count_distinct_characters(' jhrv 84 ' ) == 4
assert count_distinct_characters('') == 0
assert count_distinct_characters(' '123') == 1
```
The function takes a string and splits it into a list of characters, then creates a set of distinct characters and returns its length. The test cases cover various scenarios, passing different strings and checking the results against the expected outputs.