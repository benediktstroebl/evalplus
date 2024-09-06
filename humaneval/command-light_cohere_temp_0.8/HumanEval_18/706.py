```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding overlapping.
    : Parameters
    how many_times('abc', 'a'): 0
    :param string: str - Original string 
    :param substring: str - Substring to search 
    :return: int - Count of non-overlapping occurrences of substring in string
    """
    counter = 0
    for char in substring:
        counter += string.find(char, 1) == -1
    return counter
``` 
This function uses a counter to track how many times the substring can be found in the string without any overlapping. The function returns the string.