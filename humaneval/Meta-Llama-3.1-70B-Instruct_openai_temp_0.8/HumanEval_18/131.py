```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlaping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string.
    """
    if not substring:  # empty substring can be found 0 times
        return 0

    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1  # continue searching from the next character
        else:
            break

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes two parameters, `string` and `substring`, and returns the number of times `substring` appears in `string`, counting overlapping cases. It uses the `find` method to search for the substring in the string, starting from the last found position plus one. If the substring is not found, `find` returns -1 and the loop breaks. The test cases at the end verify that the function works correctly.