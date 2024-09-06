```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [i for i, x in enumerate(s.split('()') if x.startswith('('(',-') &)]
# Test case
def test_parse_nested_parens() -> None:
    # Sample input
    test_str = "(()()) ((())) () ((())()())"
    # Function call
    parsed_args = parse_nested_parens(test_str)
    # Check the output format and length
    assert parsed_args == [2, 3, 1, 3], "Output does not match expected format"
test_parse_nested_parens()
```
This code defines a function **`parse_nested_parens`** that takes a string as input and returns a list of integers. It performs the nested parentheses parsing, where the outermost parentheses are the deepest level. The function utilizes list comprehension to iterate over each character in the input string, checking if it starts with either "(", or ")" or "()". If the character matches either of these, it's added to the list of integers representing the depth of the innermost parentheses.