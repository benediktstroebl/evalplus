```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    count = 0
    while string:
        index = string.find(substring)
        if index!= -1:
            count += 1
            string = string[index + 1:]
        else:
            break
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses the `find` method of Python's string class to find the index of the substring in the string. It increments a counter for each occurrence and then removes the matched part of the string for the next iteration, effectively allowing for overlapping matches. The loop continues until the substring can no longer be found in the string.