### How Many Times Substring Can Be Found in the Original String
#### Problem Description
This Python script solves the problem by finding how many times a given substring can be found in the original string. The count includes overlapping cases.

#### Solution
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to be found.

    Returns:
    int: The number of times the substring can be found in the original string.

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    if not substring:  # Edge case: If substring is empty, return 0
        return 0

    string_len = len(string)
    substring_len = len(substring)

    for i in range(string_len - substring_len + 1):  # Iterate over the string
        if string[i:i + substring_len] == substring:  # Check if current substring matches
            count += 1  # Increment count if match found

    return count  # Return the total count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```
This script uses a simple iterative approach to find the occurrences of the substring in the original string. It checks each possible substring of the same length by slicing the original string and comparing it with the given substring. The count is incremented for each match found. The function returns the total count after checking all possible substrings.