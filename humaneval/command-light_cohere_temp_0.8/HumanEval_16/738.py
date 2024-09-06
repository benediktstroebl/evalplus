```python
def count_distinct_characters(string: str):
    """
    Counts the number of distinct characters in a given string, regardless of case.
    return:
    ASCII values of all uppercase, lowercase and non-alphabetic characters
    """
    return len({c for c in string.join() if c not c.isalpha() and
    additionally it be a print statement})

# Tests
string1 = "xyzXYZ"
assert count_distinct_characters(string1) == 3

string2 = "jerry"
assert count_distinct_characters(string2) == 4
```