```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.q(lowercase(c))})

# Test cases
string1 = "xyzXYZ"
string2 = "jerry"
string3 = ""

print(count_distinct_characters(string1))  # Output: 3
print(count_distinct_characters(string2))  # Output: 4
print(count_distinct_characters(string3))  # Output: 0
```