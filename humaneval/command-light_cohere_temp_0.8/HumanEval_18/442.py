```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts how many times a given substring can be found in the original string, while not Overlapping.
    Returns an count of occurrences.
    """
"""
    return: sum(1 for x in string.find(substring, 0, len(string))
    """
    return sum(1 for x in string.find(substring, 0, len(string)))

# Test the function
print(how_many_times("aaaaaa", "aa")) 
# Prints 3
```