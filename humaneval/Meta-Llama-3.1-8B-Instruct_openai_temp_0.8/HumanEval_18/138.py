```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    if not substring:  # edge case: empty substring
        return 0

    count = 0
    start = 0
    while True:
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1  # set the next start position to the one right after the found substring
        else:
            break

    return count


# Test cases
if __name__ == "__main__":
    print(how_many_times('', 'a'))  # 0
    print(how_many_times('aaa', 'a'))  # 3
    print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses the `find` method of the string class to find the positions of the substring. The `while` loop iterates over the string and counts the number of times the substring is found. The `start` variable keeps track of the position in the string where the search should start next time. If the substring is not found, the `find` method returns -1 and the loop breaks.