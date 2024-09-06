```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a given string, regardless of case.
    Args: 
    - string: str, a string to evaluate
    Returns: 
    - int: the number of distinct characters
    """
    # convert to lowercase and remove all characters not in the alphabet
    alphabet = "abcdefghijklmnopqr"
    string = [c for c in string if c in alphabet]
    return len(string)

# test the function
print(count_distinct_characters('abcX')) # 4
print(count_distinct_characters('ABC')) # 3
print(count_distinct_characters('xyzXYZ')) # 3
print(count_distinct_characters('jerry')) # 4
```