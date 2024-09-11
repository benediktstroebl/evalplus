### Substring Counting Script
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
    if not substring:  # edge case: empty substring
        return 0
    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index!= -1:
            count += 1
            index += 1  # skip to the next character
        else:
            break
    return count
```

### Example Use Cases

```python
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses the `find` method to search for the substring in the string, starting from the current index. If the substring is found, it increments the count and moves to the next character. If the substring is not found, it breaks the loop. The `if not substring:` check handles the edge case where the substring is empty, in which case it immediately returns 0.