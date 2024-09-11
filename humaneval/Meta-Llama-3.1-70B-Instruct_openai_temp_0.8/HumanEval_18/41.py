```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find.

    Returns:
        int: The number of times the substring can be found.
    """
    if not string or not substring:
        return 0

    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1

    return count


# Test cases
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
print("All test cases pass")
```

However, it's more efficient to use a single line of code using the `str.count` method is not suitable here because it doesn't count overlapping cases. We can achieve this using `re` module:

```python
import re

def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find.

    Returns:
        int: The number of times the substring can be found.
    """
    if not string or not substring:
        return 0

    return len(re.findall('(?=' + re.escape(substring) + ')', string))


# Test cases
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
print("All test cases pass")
```