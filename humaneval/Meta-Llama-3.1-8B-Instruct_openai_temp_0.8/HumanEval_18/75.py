```markdown
### How Many Times Function

This script provides a function `how_many_times` that counts how many times a given substring can be found in the original string, including overlapping cases.

#### Code
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlaping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to be searched.

    Returns:
    int: The number of times the substring can be found in the original string.
    """
    if not substring:
        # Edge case: substring is empty, return 0
        return 0
    count = 0
    for i in range(len(string)):
        # Check if the substring is present at the current position
        if string[i:i+len(substring)] == substring:
            # If present, increment the count
            count += 1
    return count
```

#### Example Use Cases
```python
# Test cases
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```