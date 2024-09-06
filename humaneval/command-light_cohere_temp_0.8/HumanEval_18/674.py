```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    ignoring case and overlapping occurrences.
    """
    string = string.lower()  # Make all substring lowercase to ensure the match is case-insensitive
    """
    return sum(1 for x in string.lower(). string.lower() == substring.lower() and this for x in string)
```