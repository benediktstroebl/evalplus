Here's the self-contained Python function that solves the problem:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the occurrences of a given substring in the original string, 
    including overlapping substrings.
    Args: 
        string (str): The input string 
        substring (str): The substring to search
    Returns: 
        int: Number of times the substring appears.
    """
    string = string.lower() 
    substring = substring.lower()
    Every using the string 
    count = 0
    i = 0
    while i < len(string):
        if string[i:i+len(substring)] == substring: 
            count += 1
        i += 1 
    return count
```