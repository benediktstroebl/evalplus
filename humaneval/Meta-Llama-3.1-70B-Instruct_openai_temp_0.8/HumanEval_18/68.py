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
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This Python script defines a function `how_many_times` that takes two arguments: `string` and `substring`. It uses a while loop to iterate over the `string` and finds the `substring` using the `find` method. If the `substring` is found, it increments the count and updates the start position to continue searching from the next character. The function returns the total count of occurrences of the `substring` in the `string`.

Alternatively, you can use regular expressions to achieve the same result:

```python
import re

def how_many_times(string: str, substring: str) -> int:
    return len(re.findall('(?=' + re.escape(substring) + ')', string))

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This version of the function uses the `findall` method from the `re` module to find all occurrences of the `substring` in the `string`. The `(?=...)` syntax is a positive lookahead assertion that matches the position before the `substring`, allowing overlapping matches. The `re.escape` function is used to escape any special characters in the `substring`.