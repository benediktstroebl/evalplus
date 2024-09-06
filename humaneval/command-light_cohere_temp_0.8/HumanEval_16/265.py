```python
def count_distinct_characters(string: str):
    """
    Returns the number of distinct characters in the given string, regardless of case.
    """
    string = 'xyzXYZ jerry zyxer'
    return len([c for c in string if c.isupper() andlower()])

# Test the function
test_string = 'xyzXYZ jerry zyxer'
assert count_distinct_characters(test_string) == 3
```