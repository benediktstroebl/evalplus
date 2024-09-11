```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

    Returns:
        int: The number of times the substring appears in the string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    if not string or not substring:
        return 0

    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1

    return count

print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

However, the above code is inefficient for large strings. We can optimize it using the KMP (Knuth-Morris-Pratt) algorithm or simply by using Python's built-in `str.find()` method in a loop. Here's a more efficient version:

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

    Returns:
        int: The number of times the substring appears in the string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    if not string or not substring:
        return 0

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

print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

But the most efficient and Pythonic way would be to use regular expressions:

```python
import re

def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

    Returns:
        int: The number of times the substring appears in the string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    return len(re.findall('(?=' + re.escape(substring) + ')', string))

print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```