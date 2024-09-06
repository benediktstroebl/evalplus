```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function to find how many times a given substring can be found in the original string, 
    accounting for overlapping matches.

    Parameters: 
    string (str): The original string 
    substring (str): The substring to search for

    Returns: 
    int: Number of occurrences of the substring in the original string
    """
    return sum(1 for s in string.cs if s == substring)
```
This Python function, `how_many_times`, is designed to determine the count of occurrences of a given substring within a given string. 

It employs a concise and efficient approach by utilizing a generator expression along with the `sum()` function. 

The function accepts two parameters: `string`, which represents the input string, and `substring`, which is the substring to search for. 

The function returns an single integer, representing the total number of occurrences of the `substring` in the `string`. 

This function can be effectively employed to solve problems involving substring matching or counting occurrences of specific patterns within a text.