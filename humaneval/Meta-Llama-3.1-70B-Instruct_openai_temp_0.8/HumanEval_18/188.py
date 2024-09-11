```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

    Returns:
        int: The number of times the substring is found in the string.
    """
    if not substring:  # if substring is empty, return 0
        return 0

    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1  # move start pointer to the next character
        else:
            break

    return count
```

You can use this function as follows:

```python
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This function uses the `find` method of the string class to find the position of the substring in the string. It keeps track of the current position in the string and moves it to the next character after each match. If no match is found, it breaks the loop and returns the count.