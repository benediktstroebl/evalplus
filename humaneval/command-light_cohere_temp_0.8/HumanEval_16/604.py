```python
def count_distinct_characters(string):
    """
    Returns the count of distinct characters in the string, regardless of case.
    """
    string = 'xyzXYZ jerry Three'
    return len([char for char in string.unique() if char not in 'abcdef'])

# Test the function
test_string = 'Jerry'
assert count_distinct_characters(test_string) == 4
```