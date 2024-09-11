```markdown
### Parse Nested Parentheses

This script calculates the deepest level of nesting of parentheses for each group in a given string.

#### Code
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    :param paren_string: A string represented multiple groups for nested parentheses separated by spaces.
    :return: A list of the deepest level of nesting of parentheses for each group.
    """
    def max_depth(s: str) -> int:
        """
        Calculate the maximum depth of nesting of parentheses in a string.

        :param s: The input string.
        :return: The maximum depth of nesting of parentheses.
        """
        max_depth = 0
        current_depth = 0
        for char in s:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_depth

    # Split the input string into groups
    groups = paren_string.split()
    # Calculate the maximum depth of nesting for each group
    max_depths = [max_depth(group) for group in groups]
    return max_depths

### Example Usage
if __name__ == "__main__":
    print(parse_nested_parens('(()()) ((())) () ((())()())'))
    # Output: [2, 3, 1, 3]
```

#### Explanation

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input. The function splits the string into groups separated by spaces and calculates the maximum depth of nesting for each group using the `max_depth` helper function. The `max_depth` function iterates over the characters in the group and keeps track of the current depth of nesting. It returns the maximum depth encountered.

The script demonstrates how to use the `parse_nested_parens` function with an example input string.