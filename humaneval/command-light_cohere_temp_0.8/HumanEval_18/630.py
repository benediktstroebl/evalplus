Here is a self-contained Python script with a function that finds the number of times a given substring can be found in the original string, while handling overlapping cases:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, 
    while counting overlapping cases.
    """
    number = 0
    for i, char in enumerate(substring):
        if char == string[i]:
            number += 1
        if char != string[i]:
            break
    return number
```