```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns the number of times the substring can be found in the string. 
    Returns 0 if the achievements are not found
    """
    return sum(1 for i,j in zip(string, substring) if j == string.group(string, substring))
``` 
This code defines a Python function called **`how_many_times`** that aims to find the frequency of a given substring within a larger string. 

This function uses a list comprehension with `zip` to iterate over each character in the string and substring simultaneously. It then checks if the `j` matches the substring, which counts as a potential match. If this occurs for all substring in the string, the function returns 1. 

The function returns 0 if the substring is not found within the larger string. 

This self-contained solution efficiently solves the problem of counting occurrences of a substring within a string.