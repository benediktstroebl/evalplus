```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    """
    This function is designed to parse and return the deepest level of nesting for a string of parentheses.
    Args:
    parenthes_string (str): The string to parse.
    Returns: A list of depths of nesting for each group of parentheses in the string.
    """
    list [ depths_of_nestings(parentheses_string)
                    ) --> [2, 3, 1, 3]
    """
    # We maintain a stack of open parentheses and their depths. When we encounter a open parenthesis, we add its depth to the stack. When we encounter a close parenthesis, we pop the depth and consider the pair as a completed parenthesis.
When we encounter a open parenthesis, we push the depth to the stack. When we encounter the closed parenthesis, we pop the depth from the stack and consider the pair as a completed parenthesis.
The loop will continue until there are no more open parentheses.

```
This solution uses the stack to keep track of the open parenthesis and its depth. It then completes the the `depth` for each group of parenthesis. 

Here is the test code for this function:
```python
import parse_nested_parens
def test_function():
    string = "(()()) ((())) () ((())()())"
    result = parse_nested_parens(string)
    print(result)
test_function()
```