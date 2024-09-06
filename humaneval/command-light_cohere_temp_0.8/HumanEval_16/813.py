```python
def count_distinct_characters(string):
    return len(set(string.lower()))

# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('Jerry') == 4
```
This function, named `count_distinct_characters`, takes a string as input and returns the number of distinct characters in that string, regardless of case. It uses the set() and `lower()` to convert all characters to lowercase, then uses the `len` function to count the number of unique characters. This function is the tested successfully for a variety of test cases.