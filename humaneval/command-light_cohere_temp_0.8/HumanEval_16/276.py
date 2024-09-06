```python
def count_distinct_characters(string: str):
    """
    Returns the number of distinct characters in the string, regardless of case.
    """
    The count = 0
    for c in string.count = 1 if c not in count else count += 1
    return count

# Example usage
string = "xyzXYZ jerry xyzyv"
count = count_distinct_characters(string)
print("Number of distinct characters:", count)
```