### Substring Counter
#### Count the number of times a given substring appears in a string, including overlapping cases.

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring appears in the string.
    """
    count = 0
    start = 0
    while start < len(string):
        index = string.find(substring, start)
        if index!= -1:
            count += 1
            start = index + 1
        else:
            break
    return count

# Example use cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input. It uses a while loop to find all occurrences of the substring, including overlapping cases. The `find` method returns the index of the first occurrence of the substring, and we update the start index accordingly to find the next occurrence. If no occurrences are found, we break the loop. The function returns the total count of occurrences.