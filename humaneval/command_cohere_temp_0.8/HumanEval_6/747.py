Here's a Python script with a self-contained function that solves the problem using a recursive solution to parse the nested parentheses:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    def max_nesting(i, nest):
        if i == len(s):
            return nest
        if s[i] == '(':
            return 1 + max_nesting(i + 1, nest + 1)
        elif s[i] == ')':
            return max_nesting(i + 1, nest)
        else:
            return max_nesting(i + 1, nest)

    return list(map(max_nesting, range(len(s)), [0] * len(s)))
```
This script uses a recursive function `max_nesting` to iterate over the string and keep track of the maximum nesting level of parentheses encountered so far at each step. The outer function `parse_nested_parens` splits the result list into individual nesting values using the `map` function.

Here's the markdown code block:
```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())()())')
    [2, 3, 1, 3]
    """

```

You can test this code block by calling the `parse_nested_parens` function with different strings to see the resulting list of deepest nesting levels for each group of parentheses.