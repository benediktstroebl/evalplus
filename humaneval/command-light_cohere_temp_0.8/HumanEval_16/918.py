```python
def count_distinct_characters(string):
    """
    Returns the number of distinct characters in the string, regardless of case.
    """
    return len([c for c in string.lower() if c not in set(string.lower())])
```
#Basic tests
test_count_distinct_characters = count_distinct_characters('xyzXYZ')
assert test_count_distinct_characters == 3

test_count_distinct_characters2 = count_distinct_characters('jerry')
assert test_count_distinct_characters2 == 4

#Test passing code for the function.
```