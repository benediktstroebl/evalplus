```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The string to be searched.

    Returns:
        int: The number of times the substring appears in the string.
    """
    if not string or not substring:
        return 0

    count = 0
    index = 0

    while index < len(string):
        index = string.find(substring, index)
        if index!= -1:
            count += 1
            index += 1
        else:
            break

    return count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that uses the `find` method of Python strings to count the occurrences of a substring within a string. It continues searching for occurrences as long as it can find them, effectively counting overlapping cases. The function then returns the count. If either the string or the substring is empty, it returns 0, as there are no occurrences in that case. The test cases at the end demonstrate the correct behavior of the function.