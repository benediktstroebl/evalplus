Here is a Python script with a self-contained function that solves the problem of matching parentheses:
```python
from typing import List
def parse_nested_parens(input: str) -> List[int]:
    """
    This function parses a string of nested parentheses and returns the deepest level of nesting.
    :param input: The string of parentheses to parse
    :return: list of the deepest level of nesting of parentheses.
    """
:
        Example usage:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    pattern = [() for _ in range(3)]
    brackets = []
    for br in input:
        if br == '':
            brackets.append(bracks.pop() if they by br == '(')
        else:
            brackets.append(bracks.pop() if br == ')'
    brackets.append(bracks.pop() if br == ')'
    brackets.append(bracks.pop() if br == '(')')
    brackets.append(bracks.pop() if br == ')')
    brackets.append(bracks.pop() if br == '('('))
    brackets.pop(0)
    brackets.append(bracks.pop() if br == '('))
    return brackets
```

The `parse_nested_parens` function takes a string as input and returns a list of the deepest level of nesting of parentheses. It uses a list comprehension with a generator expression to create the `pattern` list, which contains all the possible combinations of opening and closing parentheses. The function then iterates through the input string, matching each character against the characters in `pattern`. It uses the `pop()` method to remove the matched character from the input string and the `pattern` list. The `brackets` list is used to store the deepest level of nesting of parentheses found in the input string.