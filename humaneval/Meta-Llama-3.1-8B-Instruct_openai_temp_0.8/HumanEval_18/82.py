```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    count = 0
    if not substring:  # Handle the case when substring is an empty string
        return 0
    string_length = len(string)
    substring_length = len(substring)
    
    for i in range(string_length - substring_length + 1):
        if string[i:i + substring_length] == substring:
            count += 1
    
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```
This script defines a function `how_many_times` that takes two parameters: the original string and the substring. It iterates over the original string, checking for the presence of the substring at each position. If the substring is found, it increments a counter. After iterating over the entire string, it returns the count. The function also handles the edge case where the substring is an empty string.