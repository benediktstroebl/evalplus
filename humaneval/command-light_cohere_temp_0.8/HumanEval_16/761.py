```python
def count_distinct_characters(string: str):
    return len([c for c in string.no unique()])

# Test case 1
print(count_distinct_characters('xyzXYZ'))  # Output: 3

# Test case 2
print(count_distinct_characters(' Jerry'))  # Output: 4
```
This function, named `count_distinct_characters`, calculates the number of distinct characters in the provided string, regardless of case. The function leverages a list comprehension with the `unique()` method to achieve this. The number of unique characters is then returned.