Here's a Python script with a self-contained function that solves the problem using a recursive solution to parse nested parentheses:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses."""
    def max_depth(i, depth, char, res):
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        if depth > res[i]:
            res[i] = depth
        if depth < 0:
            return False
        if i < len(s) and (char == ' ' or char == '(' or char == ')' ):
            max_depth(i+1, depth, s[i+1], res)
        return True
    res = [0] * len(s)
    max_depth(0, 0, s[0], res)
    return res
```
The function max_depth is used as a recursive function to check the depth of each open parentheses until it reaches the deepest one. The base case happens when a closing parentheses is encountered and the depth becomes negative, in this case the function returns False indicating that this open parentheses is not part of the deepest nesting level. The max_depth function uses an auxiliary res array that holds the deepest level of each open parentheses encountered so far. When a closing parentheses is met, the depth is reduced and if it exceeds the current value of res, it's updated. The parse_nested_parens function splits the input string using spaces as separators and feeds each open parentheses to the max_depth function to obtain the deepest level of nesting for each one.