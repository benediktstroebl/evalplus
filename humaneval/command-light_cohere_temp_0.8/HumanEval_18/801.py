```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding overlapping.

    Parameters: 
    string (str): The original string 
    substring (str): The substring to search for

    Returns: 
    int: Number of occurrences of the substring in the string
    """
    return len(set(string.find(substring)))
```

Here, the function '**`how_many_times`**' uses the built-in **`find()`** method in a set to count the number of unique occurrences of the substring in the original string. This method is the more efficient and avoids the overlap of iterating the string and substring.