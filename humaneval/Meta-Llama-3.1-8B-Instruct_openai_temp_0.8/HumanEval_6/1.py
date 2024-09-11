Here's a self-contained Python script that solves the problem:
```markdown
### Nested Parentheses Parser
#### Problem Description
Parse a string of nested parentheses and return a list of the deepest level of nesting for each group.

#### Code

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    :param paren_string: A string of nested parentheses separated by spaces
    :return: A list of the deepest level of nesting for each group
    """
    groups = paren_string.split()  # Split the input string into groups
    results = []  # Initialize a list to store the results

    for group in groups:
        nesting_level = 0  # Initialize the nesting level for the current group
        max_nesting_level = 0  # Initialize the maximum nesting level for the current group

        for char in group:
            if char == '(':
                nesting_level += 1
                max_nesting_level = max(max_nesting_level, nesting_level)
            elif char == ')':
                nesting_level -= 1

        results.append(max_nesting_level)  # Append the maximum nesting level to the results

    return results

### Example Usage

print(parse_nested_parens('(()()) ((())) () ((())()())'))
# Output: [2, 3, 1, 3]
```
This script uses a simple iterative approach to parse each group of parentheses and calculate the deepest level of nesting. It splits the input string into groups, initializes a list to store the results, and then iterates over each group, keeping track of the current nesting level and the maximum nesting level seen so far. Finally, it appends the maximum nesting level for each group to the results list and returns it.