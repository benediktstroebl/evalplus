```python
def is_nested(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != brackets[char]:
                return False
    return not stack
```

The script uses a simple algorithm that takes advantage of the hierarchical structure of the problem. It uses two stacks, one for keeping track of the square brackets that have been encountered and another one for checking whether the encountered square brackets are properly nested. The algorithm iterates through the characters of the input string, if a opening bracket `([{` is met, it is pushed to the stack. When a closing bracket `)]}` is met, the algorithm checks whether the top of the stack is its matching opening bracket to verify that it is properly nested, if not the function returns False. If a closing bracket is met and the stack is empty, this means there is a closing bracket without a matching opening one, so the function returns False. If the loop completes with an empty stack, this means that all encountered brackets have been nested and the function returns True.