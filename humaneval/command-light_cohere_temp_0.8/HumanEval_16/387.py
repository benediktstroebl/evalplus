```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test cases
string1 = 'xyzXYZ'
assert count_distinct_characters(string1) == 3

string2 = 'jerry'
assert count_distinct_characters(string2) == 4

```
The above Python script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case. The test cases demonstrate the right implementation.