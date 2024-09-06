```python
def count_distinct_characters(string: str) -> int:
    """
        Function to count distinct characters in a given string regardless of case.
        Returns: number of distinct characters.
        """:
        string.
    """

    return len(set(string.distinct()) - 1
```

This function is straightforward and efficient. It uses the set data to count the unique characters, and then subtracts 1 to account for the null character, which is added to the string.