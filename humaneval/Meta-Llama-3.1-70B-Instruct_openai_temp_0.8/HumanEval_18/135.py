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
    if not substring:  # Edge case: empty substring
        return 0
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1  # Move to the next character to find overlapping matches
        else:
            break
    return count

# Test cases
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```
This script defines a function `how_many_times` that takes a string and a substring as input and returns the number of times the substring appears in the string, counting overlapping cases. The function uses a while loop to find all occurrences of the substring in the string, moving the start position one character forward after each match. The test cases at the end verify that the function works correctly for different inputs.