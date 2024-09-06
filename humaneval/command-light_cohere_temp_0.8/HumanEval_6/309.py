```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    opening_level = 0
    closing_level = 0
    result = []
    for i, char in enumerate(s):
        if char == '(':
            opening_level += 1
        elif char == ')':
            closing_level += 1
        elif opening_level > closing_level:
            stack.push = opening_level
            stack.push += closing_level
        ++ (closing_level - opening_level)
        result.append(stack.pop)
        opening_level, closing_level = 0
        stack.append(0)  # clear the stack for the next iteration
    return result
``` 
The function takes a string `s` as input and uses two stacks to keep track of opening and closing parentheses. It iterates over each string, and whenever it encounters an opening parenthesis '(', it adds one to the opening_level. Whenever it encounters a the closing parenthesis ')', it adds one to the closing_level. If the current closing_level is greater than the opening_level, the function uses the stack to calculate the difference between the two levels. This is adding up to the difference, and the function stores the result in the result list. Finally, the function resets the opening and closing levels to 0 and clears the stack. This ensures that the stack remains empty for the next iteration, and the function returns the results in the correct order.