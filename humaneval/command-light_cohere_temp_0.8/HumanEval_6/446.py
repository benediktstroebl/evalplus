Here is a self-contained Python script that solves the problem of finding the deepest level of nesting of parentheses:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    in_nest: bool = False

    for c in s:
        if c == '(' and not in_nest:
            stack.append(1)
            in_nest = True
        elif c == ')':
            if not in_nest:
                stack.pop()
            in_nest = False
        elif c == ')' and in_nest:
            stack.append(1)
            in_nest = False
        else:
            in_nest = False
            continue

    return stack
```
The function `parse_nested_parens` takes a string `s` as input, which represents multiple groups for nested parentheses separated by spaces. The function uses a stack data structure to keep track of the deepest level of nesting for each group of parentheses.

The function iterates over each character in the input string `s`. For each opening parenthesis '(', it checks if it is not nested. If it's not nested, it adds a value 1 to the stack. Then, it checks if it is a closing parenthesis ')', if it is not nested, it pops the value from the stack and resets the `in_nest` flag. If it is nested, it adds a value 1 to the stack. Then, it checks if it is a closing parenthesis ')' again, if it is nested, it adds a value 1 to the stack. The process continues until all character in the string is processed.