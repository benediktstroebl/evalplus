```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This function calculates the number of distinct characters in a given string, regardless of case. Using the `set` function with a lowercase string representation, it ensures all characters are treated equally. 

This solution provides a straightforward and effective way to address the problem of counting distinct characters in a string. You can easily utilize this code as a standalone Python script, and it can be imported and called from other scripts as needed.