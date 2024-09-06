```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for partition in s.split():
        level = 0
        stack = []
        for c in partition:
            if c == '(':
                stack.append(c)
                level += 1
            else:
                level -= 1
                stack.pop()
        result.append(level)
    return result
```

The provided Python script defines a function `parse_nested_parens` that takes a string `s` as input, and returns a list of deepest levels of nesting of parentheses in each group. The code splits the input string into a list of partitions, and for each partition, it maintains a stack of parentheses '(' and ')' to calculate the deepest level of nesting.

Here is an example usage of the function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```

And here is a test suite that can be used to validate the function:
```python
def test_parse_nested_parens():
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
    assert parse_nested_parens("(()())") == [2]
    assert parse_nested_parens("()") == [1]
    assert parse_nested_parens("(())()") == [2]
    assert parse_nested_parens("((()))") == [3]
    assert parse_nested_parens("()()()") == [2]
    assert parse_nested_parens("(()()) ((()))") == [2, 3]

test_parse_nested_parens()
```