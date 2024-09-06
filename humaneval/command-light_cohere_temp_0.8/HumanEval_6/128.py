Here is a self-contained Python script that defines a function parse_nested_parens that solves the problem of parsing and identifying the deepest level of nesting for a given string:
```python
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes in a string of parenthesis groups and returns the deepest level of nesting.
    The level of nesting in the following format: [(level, group)]
    """
    groups = []
    stack = []

    for i, char in enumerate(parent_string):
        if char == '(':
            stack.append(i)
        groups.append([stack])
        level = []
        stack.append(char)

    while char != ')':
            stack.pop()
            for j, item in stack:
                level.append(j)
                groups[item] = ' '.join(level)

    return groups
```
This function takes a string of parenthesis groups as input and returns a list of tuples where each tuple represents the deepest level of nesting for a particular group.