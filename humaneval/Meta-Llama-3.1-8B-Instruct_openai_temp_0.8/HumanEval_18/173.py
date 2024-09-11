```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

    Returns:
        int: The number of times the substring can be found in the string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    count = 0
    last_index = 0
    while True:
        index = string.find(substring, last_index)
        if index == -1:
            break
        count += 1
        last_index = index + 1
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

This script defines the function `how_many_times` that counts the occurrences of a substring in a string, considering overlapping matches. It then includes test cases to verify the correctness of the function. 

The `find` method is used with a third argument, which specifies the starting position for the search. The `last_index` variable keeps track of the position where the last match was found, and the while loop continues until no match is found. 

Finally, the script includes test cases to demonstrate the function's behavior.