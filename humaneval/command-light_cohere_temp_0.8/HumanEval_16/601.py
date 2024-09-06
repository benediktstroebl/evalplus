```python
def count_distinct_characters(string: str):
    return len(set(string))

#Tests
assertEqual(count_distinct_characters('xyzXYZ'), 3)
assertEqual(count_distinct_characters('ABC'), 3)
assertEqual(count_distinct_characters(' abcdefg'), 6)
assertEqual(count_distinct_characters(' Jerry ), 4)
```
This script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case. It then provides a tests to ensure that the function behaves correctly.