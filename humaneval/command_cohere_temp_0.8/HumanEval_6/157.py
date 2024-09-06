Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:]))), [])))) for s in s.split()]
```
The function uses two level python lists to solve this problem. The first level list is formed by splitting the input string s via space as nested parentheses are separated by spaces. The second level list is a result of mapping over the first level list, where each element is a list of characters and corresponding indices. The indices are calculated by zip(*some_list) returning a list of tuples with corresponding elements. The deepest level of nesting for each group is returned by max(...) as the maximum depth of parentheses (i.e. maximum level of nesting / 2 for even depths) for each group. The overall maximum depth of nesting is returned as a list in the end.

Here's a test to illustrate the usage of the function:
```python
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('()') == [0]
    assert parse_nested_parens('((()))') == [2]
    assert parse_nested_parens('(((())))') == [2]
    assert parse_nested_parens('(((((()))))))' ) == [4]
    assert parse_nested_parens(' ((((()())))))') == [4]
```