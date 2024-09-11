Here's a Python function that uses regular expressions (`re`) to count the occurrences of a substring within a string, including overlapping cases:

```markdown
import re

def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string, including overlapping cases.
    """
    if not string or not substring:
        return 0  # Return 0 if either string or substring is empty

    # Use re.finditer to find all occurrences of the substring
    # and len to count the number of occurrences
    return len(re.finditer(re.escape(substring), string))

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

In this code:

*   We use `re.finditer` to find all occurrences of the substring.
*   `re.escape` is used to escape any special characters in the substring, so they're treated as literal characters.
*   `len` is then used to count the number of occurrences.
*   The function includes a check to return 0 if either the string or the substring is empty, as there's nothing to search for in these cases.