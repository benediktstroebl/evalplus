```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string of nested parentheses separated by spaces as input and returns the deepest level of nesting for each group of parentheses.
    :param s: The input string of parentheses.
    :return: A list of the deepest level of nesting found in each group of parentheses
    """
    def get_max_level(s: str) -> List[int]:
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(1)
            elif ch == ")":
                stack.pop()
               max_level[stack]
                stack.append(0)
        else: stack.push(ch)
        return stack
    def parse_nested_parens(s: str) -> List[int]:
        stack = get_max_level(s)
        res = []
        for ch in s:
            if ch == "(":
                res.append(stack[-1] + 1)
            elif ch == ")":
                res.append(stack[-1])
        return res
    return parse_nested_parens('(()()) ((())) () ((())()())')')
 ``` 
This script defines a function `parse_nested_parens` that takes a string of parentheses as input and returns a list of the deepest levels of nesting found in each group of parentheses.