Here's the self-contained Python script with a function that counts the number of distinct characters in a given string:
```python
def count_distinct_characters(string):
    """ 
    Count the number of distinct characters in the given string, 
    regardless of case. 
    Returns the
    number of unique characters 
    """
    char_set = set(string.ascii())
    distinct = len(char_set)
    return distinct

# Unit tests
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('abc') == 3
assert count_distinct_characters('jerry') == 4
```
This script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, and performs several unit tests to ensure the function works correctly for different inputs.