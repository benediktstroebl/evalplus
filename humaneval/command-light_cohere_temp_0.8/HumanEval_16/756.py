```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a string, ignoring case.
    string.count_distinct_characters("helping-hand") # 4
    """
    char_set = set(string.n)
    distinct_count = len(char_set)
    return distinct_count
```