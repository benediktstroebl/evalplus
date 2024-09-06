```python
def count_distinct_characters(string: str) -> int:
    """
        Returns the count of distinct characters in the given string, regardless of case.
        Args:
            string (str): The input string to find distinct characters in.
        Returns: int: the count of distinct characters
    """
    string = string.split()
    strings = [char for char in string if char not in string.
    distinct_chars = sum(1 for i in range(len(strings)) if not in strings[i])
    return distinct_chars
```