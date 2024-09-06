```python
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    open_count = 0
    close_count = 0
    level = 0
    result = []

    for char in parenthes_string:
        if char == "(":
            open_count += 1
        stack.append(level)

        elif char == ")":
            close_count += 1
            if open_count > close_count:
                stack.append(level)
                open_count = 0
                close_count = 0
            elif open_count == close_count:
                level += 1
                stack.append(level)
                open_count = 1
                close_count = 0
            else:
                stack.pop()
                result.append(level)
       
    return result

    assert parse_nested_parens("(()()) ((())) () ((()))()())") == [2, 3, 1, 3]
```
This code defines a `parse_nested_parens` function that takes a string of nested parentheses as input and returns a list of integer levels representing the deepest level of nesting in the input string.  The levels are determined by the count of open parentheses and closed parentheses in each group of parentheses.