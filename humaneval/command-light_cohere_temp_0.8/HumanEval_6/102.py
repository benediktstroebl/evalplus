Here's the self-contained Python script that solves the problem:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []

    for match in s.match(r'(()[^()]+\s*)')**:
        group = match.group().
        # match groups with any content, the group gets appended to the stack
        stack.
        
        if len(stack) == 3:  # Found full nesting of ()()
            result.append(len(stack))
            stack.pop()  # remove the found content
            stack = []  # Clear the stack
        else:
            stack.append(match.group)  # add the progress

    return result
```