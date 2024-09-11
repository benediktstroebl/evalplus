```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring can be found in the original string.
    """
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1
        else:
            break
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines the `how_many_times` function, which takes in a string and a substring. It uses a while loop to continuously search for the substring in the string, starting from the position after the previous occurrence. If the substring is found, the count is incremented and the search starts from the next position. If the substring is not found, the loop breaks and the function returns the count. The test cases are included at the end to verify the function's correctness.