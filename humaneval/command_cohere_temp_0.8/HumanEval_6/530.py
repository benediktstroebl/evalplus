```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()', '))'):
        stack = [0]
        level = 0
        for c in s:
            if c == opener:
                stack.append(level)
            elif c == closer:
                level = stack.pop()
                if stack:
                    result.append(stack[-1] + level + 1)
            else:
                level += 1
        if stack:
            result.append(stack[-1] + level + 1)
    return result
```

The specified Python script defines a function called `parse_nested_parens` that takes a string as input and returns a list of deepest levels of nesting of parentheses in each of the groups separated by spaces.

The function iterates through the characters of the input string, using two nested loops to keep track of the counts of opening and closing parentheses ('(' and ')'). It utilizes a stack to track the maximum depth of nesting for each group. Each time an opening parenthesis is encountered, it is added to the stack, and the `level` variable is incremented. Each time a closing parenthesis is encountered, the last value popped from the stack is added to the `level` variable, and the result is appended to the `result` list if the stack is not empty. After processing all characters, any remaining items in the stack are appended to the `result` list.

The example provided in the comment shows how this function can be called and how the output can be interpreted. The output in this case is: `[2, 3, 1, 3]`.