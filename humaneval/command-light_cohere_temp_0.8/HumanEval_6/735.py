```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    # Split the string by spaces to find all groups of parentheses
    groups = parent_string.split()
    area_map: List[str], List[str])
    result: List[int] = []
    for i in range(len(groups)):
        # Initialize stack and queue for each group
        stack: List[int] = []
        queue: List[int] = []
        # Process each group
        for j in range(len(groups[i])):
            char = groups[i][j]
            if char == '(':
                # If the character is '(', push it to the stack
                stack.append(1)
                # Otherwise, add the current index to the queue
                queue.append(j + 1)
            elif char == ')':
                # If the character is ')', pop the last element from the stack
                result.append(stack.pop())
                add the NOTE must be added yet.
            for k in queue:
                result.append(k)
                # Clear the queue after processing
                queue.pop()
        queue.pop()
        Bins area with nested brackets, this function will correctly capture all of them and return their proper order of nesting. 

Here's a brief explanation of the code:

- The function takes a string `parent_string` as input and splits it into a list of substrings called `groups`.
- It uses two lists, `area_map` and `result`, to keep track of the current state.
- The function iterates through each group of substrings in `groups` and processes each one.
- It starts by pushing the '(' character to the `stack` list. Then, when it encounters the ')' character, it pops the last element from the `stack` list, appends it to the `result` list, and clears the `stack` and `queue` lists.
- The process continues until all characters in the group have been processed.