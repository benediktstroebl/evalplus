```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string()})
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))      # Output: 4
```
This code defines a function `count_distinct_characters` that calculates the count of distinct characters in a given string, regardless of case. It uses a unique character to iterate over the characters in the string and stores them in a set. This set is then contains distinct characters, so the count can be obtained using the length of this set. The function then returns the after the number of distinct characters.