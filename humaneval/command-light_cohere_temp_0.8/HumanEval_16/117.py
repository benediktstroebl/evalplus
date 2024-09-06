```python
def count_distinct_characters(string: str):
    return len(set(string))

# Test the function
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('AbcDe')
4
>>> count_distinct_characters('jerry')
4
>>> count_distinct_characters('J')
0
```