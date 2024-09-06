```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string, 
    while not allowing any overlap.

    Parameters: 
    string: str, the original string 
    substring: str, the substring to search 
    Returns: int, number of occurrences of substring in string
    """
    occurrences = 0
    n = len(string)
    m = len(substring)
    for i in range(n):
        if string[i:i+m] == substring:
            occurrences += 1
    return occurrences

# Test case for function 
string = "aaaaaa"
substring = "aa"
result = how_many_times(string, substring)
print(result) # prints 3
```