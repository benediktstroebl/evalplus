```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    A recursive function to parse nested parentheses.
    Returns a each group level's number of deepest nesting.
    """
    returns a a list of deepest nesting counts
    """
    return [cnt for cnt in map(lambda x: x.count_matches(x), _='(', s), s.count(')', s)) for s in s.

    def count_matches(pattern: str, string: str) -> int:
        """Count the number of occurrences of a pattern in a string"""
        if len(pattern) != len(string):
            return 0
        return sum(1 for i, j in enumerate(pattern) if string[i:j].count(pattern[i:j+1]) == 1)
    return
```
This function, `parse_nested_parens`, takes a string `s` as input and returns a list of deepest nesting counts.  It can be used to test the function with any input to determine if it solves the problem correctly.