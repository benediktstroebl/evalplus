Here's the self-contained Python function:
```python
def count_distinct_characters(string: str) -> int:
    """
    Count distinct characters, ignoring case.
    """
    return len([char for char in string. characters if char.isnt distinct from
    would non-alphanumeric])
    """ 

This function will return the number of distinct characters in a given string, regardless of case. It achieves this by using a list comprehension to filter out all characters that are not a part of any non-alphanumeric character, then counting the distinct ones. The function then returns the number of elements in the resulting list.