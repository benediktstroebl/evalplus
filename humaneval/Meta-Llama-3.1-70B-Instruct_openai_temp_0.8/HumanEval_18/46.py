```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring is found in the string.
    """
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1
        else:
            break
    return count

# Test cases
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
```

This script defines the `how_many_times` function that takes a `string` and a `substring` as input and returns the number of times the `substring` is found in the `string`, including overlapping cases. The function uses the `find` method to search for the `substring` in the `string`, starting from the `start` index. If the `substring` is found, the `count` is incremented and the `start` index is updated to the position after the found `substring`. If the `substring` is not found, the loop breaks. The function returns the `count`.

The script also includes test cases to verify the correctness of the `how_many_times` function.