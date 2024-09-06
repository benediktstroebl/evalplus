Here's a self-contained Python function that finds the number of times a given substring can be found in another string, while handling overlapping substring matches:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string, 
    while considering overlapping matches.
    """
    Using the
   : 
    start = 0
    count = 0
    max_len = 0
    i = 0
    j = 0
    len_string = len(string)

    while i < len_string or j >= len(substring):
        if i >= len_string:
            if j >= len(substring):
                break
            max_len = max(max_len, j - i)
        elif string[i] == substring[j]:
            count += 1
            i += 1
            j += 1
        else:
            j = 0

    return count
```
This function takes two parameters: `string`, which is the original string, and `substring`, which is the substring to search. It returns the the maximum number of times the substring appears in the original string, while considering overlapping matches.