```python
def count_distinct_characters(string):
    return len(set(string.lower()))

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
``` 
This function utilizes the `set()` method to create a set of all lowercase characters in the input string, and then uses the `len()` method to count the number of elements in the set, providing the total count of distinct characters regardless of case.