```python
def parse_nested_parens(parenthes): 
    stack = []
    for char in parenthes:
        if char == '(': 
            stack.append(1)
        elif char == ')':
            if len(stack) == 0:
                return []
            stack.pop()
       
    calculate_level()

    return [char for char in stack]

def calculate_level(level):
    if not:
        return 0
    return level + 1

# Test cases
test_parse_nested_parens = parse_nested_parens("(()) ((())) () ((()))()")

test_parse_nested_parens(')()()')

test_parse_nested_parens('(,()')

test_parse_nested_parens(')((,)())')

test_parse_nested_parens('(())()(())')

test_parse_nested_parens(')()(())()()')
```
This code provides a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest level of nesting parentheses found. The `calculate_level` function is used to calculate the level of each group of parentheses. The code also includes a series of test cases to ensure the function is working correctly.