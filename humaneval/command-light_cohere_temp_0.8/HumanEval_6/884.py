```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string of nested parentheses separated by spaces as its argument.
    It returns a levels of nesting, starting from the innermost-most nested pair and working outward.
    """
    expected input is a string with multiple groups of parentheses, separated by spaces.
    """
    Input: string with multiple groups of parentheses
    Output: list of integers representing the levels of nesting of each group
    """
    stack = []
    result = []
    for match in s:
        match = match.split("()")
        if len(match) == 1:
            result.append(len_depth(stack, match[0]))
            stack.append(match[0])
        else:
            stack.append(match[0])
            result.append(len_depth(stack, match[1]))
            stack.pop()
    stack.append(match[1])
    return result


def enclose_with_parentheses(s: str) -> str:
    """
    This function takes a string to be enclosed with parentheses as its argument.
    It returns a string with the same number of pairs of parentheses as the original string,
    with each pair of parentheses surrounding the original string.
    """
    def nest_parents(s: str) -> str:
        """
        This function takes a string with spaces around groups of parentheses as its argument.
        It returns a string with the same number of pairs of parentheses as the original string,
        but each pair of parentheses is nested inside a larger pair of parentheses.
    """ return s.replace("  "", "("). ," ") )
```
The parse_nested_parens function uses a stack to keep track of the open parentheses. It iterates over the special characters in the input string, and appends the corresponding closing parenthesis to the stack. The function then pops the last character from the stack and appends it to the result list. 

The function also uses the nested_parents function to replace any pairs of parentheses with their innermost-most nested pair, which is enclosed in a larger pair of parentheses.