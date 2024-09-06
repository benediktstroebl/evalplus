```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

string = "xyzXYZ jerry More"
print(count_distinct_characters(string))  # This will print 4
```