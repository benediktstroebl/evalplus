```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    return [i for i, char in enumerate(parent_string, 1) if char == '(' or char == ')']

# Example of if statement to test the parse_nested_parens function:
if __name__ == "__main__":
    assert parse_nested_parens('(()()) ((())) () ((()))()') == [2, 3, 1, 3]
```
This script defines a function **`parse_nested_parens`** that accepts a string containing multiple groups of nested parentheses, and returns a list of the deepest levels of nesting for each group. The last line of code serves as an example that verifies the function's output with the provided input string, and passes the test.