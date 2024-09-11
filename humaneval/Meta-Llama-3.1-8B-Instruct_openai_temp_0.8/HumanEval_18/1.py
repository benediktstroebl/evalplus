```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to be searched.

    Returns:
    int: The number of occurrences of the substring.
    """
    if not substring:
        raise ValueError("Substring cannot be empty")

    count = 0
    index = 0

    while index < len(string):
        index = string.find(substring, index)
        
        if index!= -1:
            count += 1
            index += 1  # This will match the next character after the match
        else:
            break

    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```