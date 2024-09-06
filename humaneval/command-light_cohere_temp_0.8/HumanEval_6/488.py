```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """ Parses a string of nested parentheses and returns the deepest level of nesting.
    >>>!ooooohto a way nested parentheses:
    ())()()()
    (())()()
    (())
    """
    # We keep a track of the deepest nesting level of opening parentheses we've encountered.
    # When maximum possible of opening parentheses at this level is the number of closing parentheses at the previous level.
    # If is the same for closing parentheses.
    stack: [0]  # Initial empty stack
    last_level = 0  # Index of the last non-empty element in the stack

    for i, char in enumerate(s):
        if char == '(':
            stack[-1] = i  # Move element to the right to add to the stack
            last_level = i  # Update the index of the last non-empty element to keep the stack sorted
        if char == ')':
            # If we encounter the closing parenthesis of the deepest level,
            # then push it to the stack and pop all elements from the stack up to the list of nested parentheses.
            # The stack now = stack[:stack[-1]] + stack[stack[-1:]
            last_level = stack.pop()  # Return a list of all parentheses up to this level.
        stack.append(last_level)  # Push the last non-empty element to the stack to maintain the sorted order.
    # Return the list of all parentheses up to the last non-empty element in the stack
    nested_list = []
    for last_p in stack:
        nested_list.append(last_p)  # Append the deepest level of nesting of parentheses to the list of nested parentheses
    return nested_list
```

This function parses a string of nested parentheses and returns the deepest level of nesting. It uses a type hint `List[int]` to return the deepest level of nesting. The function works by keeping track of the deepest level of opening parentheses encountered and then returns the deepest level of nesting of parentheses.