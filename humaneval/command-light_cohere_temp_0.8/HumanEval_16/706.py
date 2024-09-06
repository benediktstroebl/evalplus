```python
def count_distinct_characters(string):
    return len({c for c in string.spaces(). reasonable_to_lowercase(c) for c in string if c not in 'abcdefghijklmnopqr'tz'])

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
print(count_distinct_characters('aABC'))  # Expected output: 4
print(count_distinct_characters(' sentence'))  # Expected output: 6
print(count_distinct_characters('"/very/long""))  # Expected output: 11
print(count_distinct_characters('Hello, World!'))  # Expected output: 8
```