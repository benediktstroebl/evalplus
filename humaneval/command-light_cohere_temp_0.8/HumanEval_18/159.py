Here is a Python script with a self-contained function that solves the problem you described:
```python
def how_many_times(string, substring): 
    """ 
    Count how many times a given substring can be found in the 
    original string while not overlapping.

    Parameters: 
    string (str): original string 
    substring (sub): substring to find

    Returns: 
    count: count of occurrences of substring in string 
    """
    return len(string.find(substring, string))
```

This script has a function that finds the count of occurrences of a given substring in an original string, without overlapping. It uses the Python'sreconstruct and the find function to search for the substring in the string. It then returns the how many times the substring appears in the string without duplicates.