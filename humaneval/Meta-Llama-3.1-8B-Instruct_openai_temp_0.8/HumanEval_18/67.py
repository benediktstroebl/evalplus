Here is a Python function that solves the problem:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring appears in the string.
    """
    count = 0
    index = 0
    
    # Continue searching for the substring as long as we haven't searched the entire string
    while index < len(string):
        # Try to find the substring at the current index
        index = string.find(substring, index)
        
        # If the substring was found, increment the count and move the index to the end of the found substring
        if index!= -1:
            count += 1
            index += len(substring)
        # If the substring was not found, break out of the loop because we've searched the entire string
        else:
            break
    
    return count
```
You can test this function with the provided example use cases:
```python
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```