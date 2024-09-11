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
    count = 0
    index = 0

    # Continue searching for the substring until we've searched the entire string
    while index < len(string):
        # Check if the substring is at the current index in the string
        if string[index:index + len(substring)] == substring:
            # If it is, increment the count and move the index forward by 1
            count += 1
            index += 1
        else:
            # If it's not, move the index forward by 1
            index += 1

    return count

# Example usage:
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This Python script defines a function `how_many_times` that finds how many times a given substring can be found in the original string, counting overlapping cases. It uses a while loop to iterate over the string and checks for the presence of the substring at each position. If the substring is found, the count is incremented and the index is moved forward by 1. If the substring is not found, the index is still moved forward by 1. The function returns the total count of substring occurrences.