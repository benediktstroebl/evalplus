### How Many Times a Substring Can Be Found in a String
#### Problem Description
This script solves the problem of finding how many times a given substring can be found in the original string, including overlapped cases.

#### Solution
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

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    count = 0
    index = 0
    # Loop through the string until we've checked all possible substrings
    while index < len(string):
        # Check if the substring is present at the current index
        if string[index:index + len(substring)] == substring:
            # If it is, increment the count and move the index forward by 1
            count += 1
            index += 1
        else:
            # If it's not, move the index forward by 1
            index += 1
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```
This script works by maintaining a sliding window of the length of the substring. It then checks each position of the window to see if the substring matches. If it does, the count is incremented and the index is moved forward by 1. If it doesn't, the index is simply moved forward by 1. This process continues until all possible substrings have been checked.