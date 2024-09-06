```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.get().lower() if c != ' '})

# Test case
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```
This function, named `count_distinct_characters`, uses a generator expression to iterate over all characters in the provided string, then counts the distinct characters, regardless of case.

The output will be the number of distinct characters in the string, which is 3 for 'xyzXYZ' and 4 for 'Jerry'.