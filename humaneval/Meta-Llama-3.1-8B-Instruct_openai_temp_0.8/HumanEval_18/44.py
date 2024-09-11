```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring is found in the string.
    """
    count = 0
    # Check if the string is not empty
    if string:
        # Use the rfind function to find the last occurrence of the substring
        # Then use this result as the starting point for the next search
        # This way we can count overlapping cases
        start = 0
        while start < len(string):
            pos = string.find(substring, start)
            # If the substring is found, increment the count and move the start point
            if pos!= -1:
                count += 1
                start = pos + 1
            # If the substring is not found, break the loop
            else:
                break
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that counts the number of times a given substring appears in a string, including overlapping cases. It uses the `find` method to search for the substring, and adjusts the starting point for the next search to count overlapping cases. The function is then tested with the provided test cases.