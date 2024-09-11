```markdown
### Parse Nested Parentheses

This script parses a string of nested parentheses and returns a list of the deepest level of nesting for each group.

#### Code
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of nested parentheses

    Returns:
        List[int]: A list of the deepest level of nesting for each group
    """
    groups = paren_string.split()
    max_depths = []

    for group in groups:
        depth = 0
        max_depth = 0

        for paren in group:
            if paren == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif paren == ')':
                depth -= 1

        max_depths.append(max_depth)

    return max_depths


### Example Usage
if __name__ == "__main__":
    print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

#### Explanation
This script works by iterating over each group of parentheses in the input string. For each group, it iterates over each parenthesis and keeps track of the current depth of nesting. The maximum depth of nesting is updated whenever a parenthesis is encountered. The maximum depth of nesting for each group is then added to the output list.

#### Time Complexity
The time complexity of this script is O(n*m), where n is the number of groups and m is the average length of each group.