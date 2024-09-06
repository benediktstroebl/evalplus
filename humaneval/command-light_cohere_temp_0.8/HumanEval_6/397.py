```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == "(":  # Start of a group
          stack.push(1)
        elif c == ")":  # End of a group
          stack.pop()
        if stack:  # Process the stack
            result.append(stack.pop()
            return result
        return result
```
This function parses and returns the deepest level of nesting of parentheses in a given string. It uses a stack data structure to track the nesting of parentheses and creates the result accordingly. 

Here is the corresponding test code:
```python
def test_parse_nested_parens():
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
```
This code tests the function `parse_nested_parens` with a given input string.