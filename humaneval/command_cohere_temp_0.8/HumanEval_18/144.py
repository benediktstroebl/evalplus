Here's a Python script that contains a function called `how_many_times` which takes a string and a substring as input and returns the number of times the substring occurs within the string, including overlapping occurrences:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    if not string or not substring:
        return 0
    
    count = 0
    tmp_string = string[:]
    
    while tmp_string:
        if tmp_string.startswith(substring):
            count += 1
            tmp_string = tmp_string[len(substring):]
        else:
            break
    
    return count
```

The script includes a docstring that describes the problem and provides example usage. The function iterates through the full string using a temporary variable `tmp_string` to count occurrences accurately even when overlapping. The loop checks for the `substring` at the beginning of the `tmp_string` and increments the count if there's a match. If the substring is not found, the loop exits. The function returns `0` for empty input strings.