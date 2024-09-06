Here is a self-contained Python script that defines a function `count_distinct_characters`, which finds the count of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

#Test cases
string1 = "xyzXYZ"
assert count_distinct_characters(string1) == 3

string2 = "jerry"
assert count_distinct_characters(string2) == 4

string3 = "abc ABC"
assert count_distinct_characters(string3) == 5
```

This script provides a function that calculates the number of unique characters in a given string using the `set()` and `len()` functions. The test cases demonstrate how the example usage.