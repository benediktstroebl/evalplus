```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string.
    """
    if not substring:  # edge case: if substring is empty, return 0
        return 0

    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index!= -1:  # substring found
            count += 1
            index += 1  # move the index to the next character
        else:
            break  # substring not found, break the loop

    return count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```
This script defines the `how_many_times` function, which uses the `find` method to search for the substring in the string. The function keeps searching for the substring starting from the current index, incrementing the count each time a match is found, and moving the index to the next character after each match. If the substring is not found, the function breaks the loop. The script also includes test cases to verify the function's correctness.