Here's a self-contained Python function that solves the problem you described: 

```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    Returns a
    most deeply nested grouping of parentheses as an integer list.
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = List(map(lambda x:int((x.replace('()', ')'))) for x in parent_string.split(' ' '))
    return groups
```

This script defines a function **`parse_nested_parens`** that takes a string as input and parses it to be a list of integers. It uses a lambda function and the **`split()`** method to split the input string into individual parenthesis groups, and then uses the **`map()`** function and a list comprehension to map each group to an integer.

The resulting list of integers will contain the deepest level of nesting of parentheses in the input string.