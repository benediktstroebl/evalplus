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
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1  # Move the start position to the next character
        else:
            break
    return count


# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```
This script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring is found in the string, counting overlapping cases. The function uses the `find` method to search for the substring, and increments the count and moves the start position each time a match is found. The test cases at the end verify the function's correctness.