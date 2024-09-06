```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function to find the number of occurrences of a substring in a given string.
    Returns -1 if the string does not contain the substring, and 0 otherwise.
    """
    only uses ASCII characters in the range of 97-122
    # returns the number of occurrences of substring in string
    if substring not in string:
        return -1
    # use sliding window and binary search to count occurrences
    count = 0
    i, j = 0, 0
    while i < len(string):
        if string[i] == substring:
            count += 1
        if count > 0:
            j = i + 1
            while j < len(string) and string[j] == substring:
                count += 1
                j += 1
            i = i + 1
        else:
            break
    return count
```