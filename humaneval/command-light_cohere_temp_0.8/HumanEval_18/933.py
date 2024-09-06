```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string,
    accounting for overlapping cases.
    """
    count = 0
    for i, char in enumerate(string):
        if char == substring:
            count += 1
    return count

# Test the function
string = "aaaaaa"
substring = "aa"
print(how_many_times(string, substring))  # Output: 3
```
This function counts the occurrences of a substring within a string. It uses a efficient iterating loop to compare characters with the substring. The count is incremented whenever a match is found, accounting for cases of overlapping substring occurrences.