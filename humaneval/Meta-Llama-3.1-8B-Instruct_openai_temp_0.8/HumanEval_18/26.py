```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the string.
    """
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

This script defines the `how_many_times` function, which uses a while loop to find all occurrences of the substring in the string. The `find` method returns the index of the first occurrence of the substring, or -1 if it's not found. If the substring is found, the function increments the count and moves the index to the end of the matched substring. If the substring is not found, the function breaks out of the loop and returns the count. 

The test cases are included at the bottom of the script to demonstrate how the function works.