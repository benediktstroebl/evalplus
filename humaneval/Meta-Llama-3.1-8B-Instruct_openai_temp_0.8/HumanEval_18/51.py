### How Many Times a Substring Can Be Found in a String
#### Problem Description
The function `how_many_times` finds how many times a given substring can be found in the original string, including overlapping cases.

#### Code
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    count = 0
    # If the substring is empty, there's no way to match it, unless the string is empty
    if not substring:
        return 1 if not string else 0
    # Iterate over the string with a sliding window of the substring's length
    for i in range(len(string) - len(substring) + 1):
        # Check if the current window matches the substring
        if string[i:i + len(substring)] == substring:
            # If it does, increment the count
            count += 1
    # Return the total count
    return count

# Example usage
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```
This script defines the `how_many_times` function, which iterates over the string with a sliding window of the substring's length, checking each window for a match. If a match is found, the count is incremented. The total count is then returned. The example usage demonstrates the function's behavior with different inputs.