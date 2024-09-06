Here is a self-contained Python script that defines a function `count_distinct_characters` solving the problem you have described:

```python
def count_distinct_characters(string: str) -> int:
    """
    Count distinct characters, ignoring case.
    Convert all characters to lowercase to make the comparison case-insensitive
    """
    string = string.lower()
    unique = set(string)
    return len(unique)
```

This function takes a string as an argument and returns the number of distinct characters in that string, converted to lowercase to make the comparison case-insensitive. 

The function is designed to be easy to understand and to be efficient, with a time complexity of O(1).  You can use this script and the function `count_distinct_characters` to solve your problem.