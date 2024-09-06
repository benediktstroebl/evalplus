```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()})
 important note that it does not consider case sensitivity.
xXYZ = "xyzXYZ"
print(count_distinct_characters(xXYZ))  # Output: 6

Jerry = "jerry"
print(count_distinct_characters(Jerry))  # Output: 4
```