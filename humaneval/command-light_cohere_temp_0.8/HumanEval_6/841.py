```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    opening_level = 0
    closing_level = 0
    nesting_levels = 0

    for char in parentheses_string:
        if char == '(':
            opening_level += 1
            stack.append(nesting_levels)
            nesting_levels = 0
        elif char == ')':
            closing_level += 1
            if opening_level == closing_level:
                stack.append(nesting_levels)
                opening_level = 0
                closing_level = 0
                nesting_levels = 0
        elif opening_level > closing_level:
            stack.append(nesting_levels)
        stack.append(char)

    nested_parens = [level for level in stack if level > 0]
    return nested_parens
``` 
The provided function `parse_nested_parens` takes a string of nested parentheses as input and returns a list of integers that represents the deepest level of nesting of parentheses in the string. This function uses a nested stack to keep track of opening and closing parentheses and their nesting levels.  The time a open parentheses, it increments the opening_level and pushes the current nesting level into the stack. When a closing parenthesis is encountered, it increments the closing_level. If the opening and closing levels match, it pushes the nesting level from the stack back into the variable `nesting_levels` and resets the opening and closing levels to 0. 

The function then iterates over the characters in the string and uses the stack to keep track of the deepest level of nesting. The function then reaches the end of the string, returns the list of integers that represents the deepest level of nesting of parentheses in the string.