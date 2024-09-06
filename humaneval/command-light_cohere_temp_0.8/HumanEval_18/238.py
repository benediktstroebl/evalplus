Here is a self-contained Python script that defines a function to solve the problem of counting the frequency of a substring within a given string:
```python
import re
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string,
    counting overlapping matches.
    """

    return sum(1 for m in re.finditer(subpattern, string))
```
The function uses the `re` module in Python for efficient pattern matching. The function returns the how many times the substring appears in the original string.