### Nested Parentheses Parser

Below is a Python script that defines a function to parse nested parentheses and calculate the maximum level of nesting within each group.

```markdown
### Code
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses as input, 
    separated by spaces. It then calculates the maximum level of nesting 
    within each group and returns these levels as a list.

    Args:
    paren_string (str): A string of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of maximum levels of nesting within each group.
    """
    def calculate_depth(paren_str: str) -> int:
        """ Helper function to calculate maximum depth of nesting. """
        depth = 0
        max_depth = 0
        for char in paren_str:
            if char == '(':
                depth += 1
            elif char == ')':
                max_depth = max(max_depth, depth)
                depth -= 1
        return max_depth

    result = []
    # Split the input string into groups and calculate depth for each group
    for group in paren_string.split():
        result.append(calculate_depth(group))
    return result


### Example Usage
if __name__ == "__main__":
    print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

### Explanation

1. The function `parse_nested_parens` takes a string of nested parentheses as input and splits it into individual groups.
2. For each group, it calculates the maximum level of nesting using a helper function `calculate_depth`.
3. The `calculate_depth` function iterates through the characters in a group, incrementing the depth when encountering an open parenthesis and decrementing when encountering a close parenthesis. It keeps track of the maximum depth encountered so far.
4. Finally, the function returns a list of maximum levels of nesting for each group.

### Running the Script

Save this script to a file (e.g., `nested_parentheses.py`) and run it using Python 3.x: `python nested_parentheses.py`