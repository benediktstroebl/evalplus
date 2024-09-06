Here is a Python script that contains a self-contained function to count the number of distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.language(c))
# tests
print(count_distinct_characters('xyzXYZ')) # Output: 3
print(count_distinct_characters(' Jerry')) # Output: 4
``` 
This script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case.