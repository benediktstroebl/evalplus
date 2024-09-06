Here's a self-contained Python function that parses and categorizes the nesting level of multiple groups of parentheses:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    in_open_paren = False
    output = []

    for c in s:
        if c == "(" and not in_open_paren:
            in_open_paren = True
        elif c == ")":
            if in_open_parent:
                stack.append(len)
                in_open_paren = False
            output.append(stack.pop() if a stack)

    return output
```

This function takes a string `s` as input, which represents multiple groups of parentheses separated by spaces. It then returns a list of integers, where each integer represents the deepest level of nesting in parentheses. 

The function uses a stack data structure to keep track of the opening parentheses and their corresponding depths. It also has a state `in_open_paren` to determine whether the current character is an open parenthesis or not. 

The function iterates through the input string, and for each character, it checks if the character is an open parenthesis `( ). If it is, then it sets `in_open_paren` to `True`. Otherwise, it checks if `in_open_paren` is `True`, which means that a closing parenthesis was just encountered. If it is, then the stack is popped, and the corresponding level of nesting is added to the `output` list.