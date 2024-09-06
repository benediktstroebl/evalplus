Here's the self-contained Python script with a function that solves the problem of counting occurrences of a substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    including overlapping matches.
    Parameters: 
    string (str): The input string 
    substring (str): The substring to find in the string 
    Returns: 
    int: Number of times the substring appears in the string
    """
    return sum(1 for _ in string.find(substring, string))
```
This script defines a function that iterates over each character in the input string and counts the number of occurrences of the specified substring, including overlapping matches.