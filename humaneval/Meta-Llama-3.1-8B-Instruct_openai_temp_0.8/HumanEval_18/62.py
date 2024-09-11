```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be found.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    if not substring:  # edge case: empty substring
        return 0
    count = 0
    start = 0  # start index for searching
    while start < len(string):
        pos = string.find(substring, start)  # find the position of the substring
        if pos!= -1:  # if the substring is found
            count += 1  # increment the count
            start = pos + 1  # move the start index to the next character
        else:
            break  # if the substring is not found, break the loop
    return count

# test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes two arguments: `string` and `substring`. It then uses a while loop to find all occurrences of `substring` in `string`, counting overlapping cases. The function returns the count of occurrences. The script also includes test cases to verify the function's correctness.