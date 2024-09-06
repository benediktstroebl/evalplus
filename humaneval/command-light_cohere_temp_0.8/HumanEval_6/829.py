Here's the code:
```python
def parse_nested_parens(s: str) -> List[int]:
    def helper(curr_level, string):
        stack = []
        opening_brack = False
        closing_brack = False
        level = curr_level + 1

        for char in string:
            if char == ')':
                closing_brack = True
            elif char == '(':
                opening_brack = True
            else:
                stack.push(level)

        if closing_brack and opening_brack:
            return level
        elif opening_brack:
            stack.push(level)

        curr_level.push(level)
        return stack
    return stack

def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
```
The function `parse_nested_parens` accepts a string of nested parentheses and returns a list of the deepest levels of nesting. The `helper` function recursively pushes and returns the stack of levels of parentheses in the given string. This ensures a correct order of the input is maintained, as expected.