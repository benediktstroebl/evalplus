### Find Substring Occurrences in a String
#### Problem Description
The `how_many_times` function counts the occurrences of a given substring in an original string, considering overlapping cases.

#### Solution
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to search for.

    Returns:
    int: The number of occurrences of the substring in the string.

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not substring:  # edge case: empty substring
        return 0

    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index!= -1:  # found a match
            count += 1
            index += 1  # move to the next character
        else:
            break

    return count
```
This script defines a function `how_many_times` that takes two string arguments: the original string and the substring to search for. It returns the number of occurrences of the substring in the string, considering overlapping cases. The function uses a while loop to iterate through the string and finds the substring at each position using the `find` method. If a match is found, it increments the count and moves to the next character. If no match is found, it breaks out of the loop and returns the count. The script includes a docstring with examples and edge cases.