```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts the number of times a given substring can be found in the original string.

    Args:
        string (str): The input string
        substring (sub): The substring to find

    Returns:
    count: Number of times the substring appears in the string
    """
    return len(set(string.find(substring)))
```

This Python script defines a function `how_many_times` that counts the number of occurrences of a given substring within a given input string. The function utilizes the find() function with a lambda to search for all occurrences of the substring in the string, and then uses the set() function to create a unique set of characters that are present in the string. Finally, the len() function is used to count the number of unique characters in the set, which corresponds to the number of occurrences of the substring in the string.