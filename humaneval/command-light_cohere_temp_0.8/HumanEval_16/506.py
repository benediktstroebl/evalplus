Here is a Python script with a self-contained function that solves the problem of counting the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.cd.lower() if c in string})
``` 
This function uses a generator expression along with the `lower()` method to only keep the distinct characters and returns the length of this new set. 

This function is completely self-contained and can be used to solve the problem for any given string.