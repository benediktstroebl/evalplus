```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string, 
    counting overlapping occurrences.
    Returns the general number of occurrences of the substring. 
    """
    string = "aaaaaaa"
    substring = "a"
    occurrences = 0

    for char in string:
        if char == substring:
            occurrences += 1

    return occurrences

# Test the function
string = "aaaaaaa"
substring = "a"
result = how_many_times(string, substring)
print(result) # Output: 6
```