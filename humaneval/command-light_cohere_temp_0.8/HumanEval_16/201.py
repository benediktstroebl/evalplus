```python
def count_distinct_characters(string: str) -> int:
    return len([c for c in string. distinct()])

# Tests
string = 'xyzXYZ'
print(count_distinct_characters(string))  # Output: 3

string = 'jerry'
print(count_distinct_characters(string))  # Output: 4

# Test case with non-alphanumeric characters
string = 'jerry#pmn'
print(count_distinct_characters(string))  # Output: 3
```