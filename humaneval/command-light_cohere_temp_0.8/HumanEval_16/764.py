Here's the provided Python code with a self-contained function that finds the count of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    """
    Returns the count of distinct characters in the given string, regardless of case.
    """
    string = "xyzXYZ jerry jfooval zx ACM"
    char_set = set(string)
    distinct_count = len(char_set)
    return distinct_count
```
This function utilizes the `set` method to create a set of characters from the input string, then calculates the count of distinct characters using the `len` function. 
The output is the count of distinct characters.