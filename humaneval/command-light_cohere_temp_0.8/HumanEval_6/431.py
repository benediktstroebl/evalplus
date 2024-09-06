```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes a string with multiple groups of nested parentheses separated by spaces as input and returns the deepest level of nesting of parentheses.
    """
    example input: ((()))()()()()()()()()()()()()())
    """
    parents: List[str] = list(parent_string.split())
   
    smallest_parent: str = parents[0]
    nest: List[str] = []
    for parent in parents[1:]:
        if parent == '(':
            nest.append('(')
        else:
            nest.append(parent)
        if len(nest) == 0:
                nest.append(')')
                smallest_parent += '('
                if len(nest) == 0:
                    nest.append(')')
                smallest_parent = nest
            nest = [parent] + nest[::-1]
        else:
            nest.append('(')
    smallest_parent = parent
    return nest


def test_parse_nested_parens():
    test_str = "((()))()()()()()()()()()()"
    nest = parse_nested_parens(test_str)
    assert nest == [2, 3, 1, 3]
```