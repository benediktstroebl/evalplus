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
    count = 0  # Initialize count variable
    index = 0  # Initialize index variable
    if not substring:  # If substring is empty
        return len(string)  # Return the length of the string
    while index < len(string):  # Loop through the string
        index = string.find(substring, index)  # Find the substring
        if index!= -1:  # If the substring is found
            count += 1  # Increment the count
            index += 1  # Move the index forward
        else:
            break  # Break the loop if the substring is not found
    return count  # Return the count


# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```