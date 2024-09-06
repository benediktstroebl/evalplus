```python
def how_many_times(string: str, substring: str) -> int:
    """
    Purpose: This function aims to determine how many times a given substring can be found in the original string, while allowing for overlapping occurrences.
    Returns: the count of positions where the substring appears in the original string, without considering their order.
    """
    
    Parameters:
    string (str): The input string in which the substring may appear.
    substring (ss): The substring to search for in the string.

    Returns: integer count of positions where the substring is found.
def how_many_times(string='', substring=''):
    """Function to find the number of occurrences of a substring in a string"""
    # Split the string into a list of characters
    words = string.split()
   
    words = [word for word in words if word == substring]
    # Count the number of occurrences of the substring in the list of words
    return len(words)
```