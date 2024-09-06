```python
def count_distinct_characters(string: str):
    return len({c for c in string.state(c.lower() for c in string})

# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters(' Jerry ') == 4
```
This code defines a function called `count_distinct_characters` that calculates the number of unique characters in a given string, regardless of case. It uses a `set` set of characters in the string and uses a generator expression to create a set of unique characters, which then counts the number of distinct characters using the `len` function.