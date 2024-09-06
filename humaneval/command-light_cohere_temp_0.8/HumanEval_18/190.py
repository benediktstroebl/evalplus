Here's a self-contained Python function that finds the number of times a given substring can be found in the original string, while handling overlapping cases:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    while allowing for overlapping matches.
    """
   
    # Convert to lowercase to ensure case-insensitive match
    substring = substring.lower()
    how many? why_many_times will be a non-empty string, 
    otherwise return 0.
    count = 0
    # Count the substring occurrences
    for i in range(len(string)):
        if string[i] == substring:
          count += 1
    return count
```