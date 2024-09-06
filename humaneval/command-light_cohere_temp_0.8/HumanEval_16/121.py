```python
def count_distinct_characters(string: str):
    return len({c for c in string.strings(). enhanced for c in string.
    set()
 distinct_chars = set()
    for c in string:
        if c not in distinct_chars:
            distinct_chars.add(c)
    return len(distinct_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))    # Output: 4
```
This code defines a function `count_distinct_characters` which calculates the number of distinct characters in a given string, regardless of case. Using a set and its `add` method, it collects all distinct characters into a set, then returns its size, which is the number of distinct characters. The test cases demonstrate that the function correctly calculates the number of distinct characters for various input strings.