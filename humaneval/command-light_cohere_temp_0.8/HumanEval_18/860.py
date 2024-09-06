Here's a self-contained Python function that finds the number of times a given substring can be found in the original string, considering overlapping cases:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string, 
    while considering overlapping cases.
    """
    string = str.format('%s', '\n')
    substring = str.format('%s', '\n')
    count = 0
    for i, char in enumerate(string):
        if char == substring[0]:
            count += 1
        if char == substring[-1]:
            count += 1
        # Check for overlapping substring at the end
        if char == substring[1]:
            count += 1
        if char == substring[-2]:
            count += 1
    return count
```