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
        elif not stack:
            return False
    return not stack
```

The function employs a stack to keep track of the brackets encountered. When a closing bracket is met, it checks if it matches the most recent opening bracket on the stack. If they don't match or if the stack is empty, the function returns False, indicating no valid nested brackets. Otherwise, it proceeds with the loop, ensuring all brackets match appropriately.

The solution is optimized for efficiency, as it only needs to verify the correctness of each bracket as it iterates through the string. This linear time solution is an optimized approach compared to possible brute force methods.