Here is a Python script that contains a self-contained function that solves the problem:
```python
def how_many_times(string, substring): 
    """ Count how many times a given substring can be found in the original string, 
    ignoring case and overlapping characters.

    Args:
        string (str): Original string 
        substring (ss): Substring to find in the original string

    Returns: 
    int: Number of occurrences of substring in the original string 
    """
    return len(string.find(substring, case=False))
```
This script defines a function that returns the number of occurrences of a given substring in a string, ignoring case and overlapping characters. The function uses the find method to search for a substring in the string, and uses the len function to return the number of matches found.