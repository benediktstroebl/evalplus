Here's the improved code:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding duplicates.

    :
    for i, char in substring: 
        if char in string: 
            count += 1 
            if count == len(substring): 
                return count 
        string += ' ' + char
    return 0
```