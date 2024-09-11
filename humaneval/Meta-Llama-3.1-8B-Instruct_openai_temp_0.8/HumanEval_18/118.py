```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to be searched.

    Returns:
    int: The number of times the substring can be found in the original string.
    """
    count = 0
    if not substring:  # if substring is empty, return 0
        return 0
    string_length = len(string)
    substring_length = len(substring)
    for i in range(string_length - substring_length + 1):  # loop through the string
        if string[i:i + substring_length] == substring:  # check if the substring matches
            count += 1
    return count
```

You can use this function to find how many times a given substring can be found in the original string, including overlapping cases. 

Here's how you might test it:

```python
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```