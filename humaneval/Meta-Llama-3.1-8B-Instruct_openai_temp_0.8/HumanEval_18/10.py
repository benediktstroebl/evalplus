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
    if not substring:
        return 0  # Edge case: substring is empty

    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index!= -1:
            count += 1
            index += 1  # Move to the character after the found substring
        else:
            break

    return count
```

You can test this function with the provided examples:
```python
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```
This function uses a while loop to continuously search for the substring starting from the current index. When the substring is found, it increments the count and moves to the character after the found substring. If the substring is not found, it breaks out of the loop and returns the count.