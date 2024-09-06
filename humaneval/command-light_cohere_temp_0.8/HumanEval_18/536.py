```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    taking overlapping occurrences into account.

    Args: 
    - string (str): The original string 
    - substring (str): The substring to search for
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test code goes here, to demonstrate function working 
    assert how_many_times('aaaa', 'aa') == 3
```