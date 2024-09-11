### How Many Times Substring Appears in String
#### Problem Description
This script provides a function to count the number of times a given substring appears in an original string, considering overlapping cases.

#### Python Script
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string.
    """
    count = start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            start = pos + 1
            count += 1
        else:
            break
    return count

# Example Usage:
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```
This script uses a while loop and the built-in `find()` method of Python strings to efficiently find the occurrences of the substring. It starts at the beginning of the string and keeps searching as long as it finds the substring. The position where the substring is found (`pos`) is used to determine the next position to search from.