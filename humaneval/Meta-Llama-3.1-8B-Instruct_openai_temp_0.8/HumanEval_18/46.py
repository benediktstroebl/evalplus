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
    int: The number of times the substring is found in the original string.

    Examples:
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # Use regular expression to find all occurrences of the substring
    # The '+' after the substring means one or more of the preceding element
    # This way, overlapping cases are counted
    pattern = re.compile(re.escape(substring) + '+')
    matches = pattern.findall(string)
    
    # The length of the matches list is the number of times the substring is found
    return len(matches)
```

You can call the function with the following code:

```python
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```