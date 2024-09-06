```python
def count_distinct_characters(string: str):
    return len(set(string))

# Test the function:
 assert count_distinct_characters('xyzXYZ') == 3
 assert count_distinct_characters('jerry') == 4
```