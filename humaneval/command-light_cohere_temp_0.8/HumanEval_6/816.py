```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    def nested_levels(current_level: int, string: str) -> int:
        nonlocal levels
        count = 0
        for char in string:
            if char == '(':
                count += 1
                levels[current_level] += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    levels[current_level] -= 1
                if levels[current_level] > 0:
                    levels[current_level] -= 1
                else:
                    break
        return count

    levels = [0]
    return nested_levels(0, parenthesis_string)

def test_parse_nested_parens():
    assert parse_nested_parens('(()) ((())) () ((())()())') == [2, 3, 1, 3]
```
This code defines a function `parse_nested_parens` that returns a list of the deepest level of nesting for each group of parentheses in a string. The function uses a nested list `levels` to keep track of the depth of each nesting level. The `test_parse_nested_parens` function is used to run a test on the `parse_nested_parens` function with a sample input.