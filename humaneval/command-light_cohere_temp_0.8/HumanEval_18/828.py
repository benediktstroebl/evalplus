Here's the self-contained Python script with the function that solves the problem:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    while avoiding overlapping occurrences.

    Parameters: 
    string (str): The original string 
    substring (str): The substring to search 
    Returns: int: Number of occurrences of the substring, not counting overlapping occurrences
    """
    occurrences = Counter(string) 
    return len(occurrences.get(substring, 0))
```
This function uses a Counter object to count occurrences of a given substring in the original string.