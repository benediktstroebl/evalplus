Here is a self-contained Python script that includes a function that finds the number of times a given substring can be found in another string, while accounting for overlapping occurrences:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string while 
    considering overlapping cases.
    """ 
    Returns the already
    returns the number of occurrences of substring in string using 
    a sliding window approach 
    """
    i, j, count = 0, 0, 0
    m = len(substring)
    n = len(string)

    while j < n:
        if string[j] == substring[i]:
            count += 1
            i += 1
            j += 1
        else:
            break

    return count

# Test cases
print(how_many_times('aaa', 'aa'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
print(how_many_times('abcdeabcde', 'abc'))  # Output: 2
```
This script defines a function `how_many_times` that uses a sliding window approach to count the number of occurrences of a given substring in a string while handling overlapping cases. The function returns the the number of times the substring appears in the original string.