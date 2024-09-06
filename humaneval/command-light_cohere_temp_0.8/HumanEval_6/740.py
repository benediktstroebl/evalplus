Here is a self-contained Python script that solves the problem:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    n: int = 0
    result: List[int] = []
    for i, char in enumerate(s):
        if char == '(':
            n += 1
            stack.append(n)
        else:
            n -= 1
            if n < 0:
                result.append(stack.pop())
            else
                stack.append(i)
    a = []
    return result
```

This function takes a string `s` as input, and it uses a stack to keep track of the opening parentheses. It then iterates through characters of the string, and for each character, it checks if it's an opening parenthesis, in which case it pushes the current nesting level onto the stack and continues iterating. If it encounters aver closing parenthesis, it pops the entire group from the stack, and appends it to the result list. This process continues until all string has been fully parsed.