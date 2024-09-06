```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []
    for match in parentheses_string.match(r'(',')(...*')]+):
        if match.group(0) == '(':
            stack.append(1)
        else:
            stack.append(int(match.group(0)))
        if match.group(2) == '(':
            stack.append(2)
        else:
            stack.append(int(match.group(2)))
        if match.group(3) == '(':
            stack.append(3)
        else:
            stack.append(int(match.group(3)))
    while:
            if stack and match.group(0) != '(':
                result.append(stack.pop())
                stack)
            return result
```
This Python script defines a function `parse_nested_parens` designed to parse a string of nested parentheses. The function uses the `match` module to find matches of regular expressions. The function works by iterating through matches of parentheses in the string. It uses a `stack` list to keep track of open parentheses. The function then iterates through the matches and appends appropriate values to the `stack` list. The function also appends values to the `result` list that match the deepest level of nesting of parentheses. The function returns the `result` list.