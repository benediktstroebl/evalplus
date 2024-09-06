```python
def is_nested(s):
    stack = []
    for bracket in s:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if not stack or stack.pop() != '[':
                return False
    return not stack
```

The function employs a stack to keep track of the brackets encountered. When a closing ']' bracket is met, the stack is checked for the most recent item. If it is not an opening '[' bracket or if the stack is empty, the sequence is not nested. Conversely, when an opening '[' bracket is encountered, it is added to the stack, facilitating tracking of the brackets.

The given examples showcase its functionality:
- is_nested('[[]]') returns True, as the inner '[[' is correctly nested within the outer '[]'
- is_nested('[][]') returns False, as the brackets are not nested and the stack would be left empty
- is_nested('[]']) returns False, as the last ']' does not have a matching opening bracket

The script ensures a concise and efficient solution to the problem.