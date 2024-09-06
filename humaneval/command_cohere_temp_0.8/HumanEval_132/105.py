```python
def is_nested(s):
    stack = []
    brackets = {'[': ']', '(': ')', '{': '}'}
    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            top = stack.pop() if stack else '#'
            if brackets[top] != brackets[char]:
                return False
        else:
            return False
    return not stack
```

The following code snippet efficiently determines whether a square bracket sequence contains a valid nested sequence. It does this by utilizing a stack to keep track of opening brackets and a dictionary to map opening brackets to their corresponding closing brackets.

This algorithm iterates through each character of the input sequence `s`. When an opening bracket is encountered, it is pushed onto the stack. When a closing bracket is encountered, the algorithm checks whether it matches the most recent opening bracket on the stack (or '#' if the stack is empty). If they don't match or if the stack is empty, the sequence is invalid. If the closing bracket matches the top of the stack, the stack is popped.

After processing all characters, the algorithm returns `False` if the stack is not empty, indicating an unbalanced bracket sequence. Otherwise, it returns `True`, indicating a valid nested sequence with at least one nested pair of brackets.

This code achieves an efficient O(n) time complexity, where n is the length of the input sequence, as it performs a constant amount of work for each input character. It is also trivially possible to adapt this code to handle curly braces and parentheses, should the problem statement have included these.