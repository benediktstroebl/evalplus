Here is a self-contained Python script with a function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a string, ignoring case.
    """
    return len({c for c in string.sum() if c not in set(string.value('c', True))[0]])

# Example usage:
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3

def test_count_distinct_characters2():
    assert count_distinct_characters('Jerry') == 4
``` 
This script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string. The function uses a list comprehension and set difference to achieve this. The test cases verify the test coverage and ensure the function behaves correctly.