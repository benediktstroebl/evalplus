```python
def count_distinct_characters(string):
    """
    Returns the count of distinct characters in the given string, regardless of case.
    Args: 
    - string: str, the input string containing characters only 
    Returns: 
    int, the count of distinct characters 
"""
    string = string.lower()  #replace(string)
    string = ''.join(string)
    return len(set(string))

# Test case 1
print(count_distinct_characters('xyzXYZ'))  # Output: 3

# Test case 2
print(count_distinct_characters('jerry'))  # Output: 4
```
This function is self-contained, and it efficiently calculates the count of distinct characters in a given string, regardless of case.