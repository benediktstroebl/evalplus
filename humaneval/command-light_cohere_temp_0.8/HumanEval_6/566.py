```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function is designed to parse and return the deepest level of nesting of parentheses in the input string.
    :

    It specific to handling multiple groups of nested parentheses separated by spaces.

    : Return a list of the highest nesting level of parentheses.
    :param s: The input string containing multiple groups of parentheses
    :return: A list of integer representing the deepest level of nesting
    """
    res: List[int] = []
    for group in s.group: :
        if group == '(':
            res.append(1)
        else:
            res.append(max(res)+1)
    return res

# Example test cases
test_cases = [
    "(()()) ((())) () ((()))()",
    "()()((()))",
    "((()))()()()()()()()()()()",
    "((())) (( ((())))) ",
    "((()()()))",
    "())()()()()"
]

for case in test_cases:
    actual = parse_nested_parens(case)
    assert actual == [1, 3]  # [ deepest level of nesting is 4 ]
```
This code defines a function called `parse_nested_parens` that takes an input string as its parameter and returns a list of integers. It uses a specific logic to handle the nested parentheses in the input string, with the ability to handle multiple groups of parentheses separated by spaces.