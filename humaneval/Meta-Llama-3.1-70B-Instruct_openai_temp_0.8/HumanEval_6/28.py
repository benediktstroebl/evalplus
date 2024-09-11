Here is a self-contained Python script that solves the problem using a stack data structure.

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split()
    results = []

    for group in groups:
        stack = []
        max_depth = 0
        for char in group:
            if char == '(':
                stack.append(char)
                max_depth = max(max_depth, len(stack))
            elif char == ')':
                stack.pop()
        results.append(max_depth)

    return results

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

In this script, we define the function `parse_nested_parens` with the specified signature. This function works as follows:

1.  Split the input string into separate groups based on spaces.
2.  Iterate over each group.
3.  Initialize an empty stack (`stack`) to track the nesting level of parentheses.
4.  Iterate over each character in the group.
5.  When an open parenthesis `(` is encountered, push it onto the stack and update the maximum depth (`max_depth`) if necessary.
6.  When a close parenthesis `)` is encountered, pop the corresponding open parenthesis from the stack.
7.  After processing the entire group, append the maximum depth (`max_depth`) to the results list.
8.  Finally, return the list of maximum depths for all groups.

The example usage demonstrates how to use the function with the provided example input and prints the expected output: `[2, 3, 1, 3]`.