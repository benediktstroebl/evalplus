```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to be searched.

    Returns:
    int: The number of times the substring is found in the string.
    """
    if not substring:  # edge case: empty substring
        return 0

    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1  # move the start pointer to the next character
        else:
            break
    return count

# test cases
print(how_many_times('', 'a'))   # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```
This script defines a function `how_many_times` that takes two strings as input, `string` and `substring`. It uses a while loop to find the substring in the string, starting from the current position `start`. If the substring is found, it increments the count and moves the start pointer to the next character. If the substring is not found, it breaks the loop. The function returns the count of times the substring is found in the string.