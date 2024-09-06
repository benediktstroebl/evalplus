Here's the provided Python script that showcases your solution to the problem described:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Function to find how many times a given substring can be found in the original string. 
    Count overlapping substring cases. 
    """ 
    Returns function a standard case, the solution is to use the sliding window approach using 
    itertools.
    """
    multise across thes of substrings using 1 index difference each time.
    """ 
    Return with overlapping substring cases, 
    the length of the longest substring is the solution.
""" 
    # Initialize variables
    total = 0
    i, j = 1, 0

    # Sliding window function
    while i < len(string):
        while j < i and substring[j] == string[i]:
            j += 1
        total = max(total, j - i + 1)
        i += 1

    return total
``` 
Do you need anything else?