```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlaping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be found.

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
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

This script defines a function `how_many_times` that takes two string arguments: `string` and `substring`. It returns the number of times `substring` can be found in `string`, counting overlapping cases.

The function uses a while loop to iterate over the `string`. In each iteration, it finds the position of `substring` in `string` starting from the current position `start`. If `substring` is found, it increments the count and updates `start` to the position after the found `substring`. If `substring` is not found, it breaks the loop.

The test cases at the end of the script demonstrate the function's behavior with the expected outputs.