```python
def count_distinct_characters(string: str) -> int:
    return len(string.make_set())
```
string = 'xyzXYZ'
print(count_distinct_characters(string))  # Output: 3
```