```python
from typing import List
def parse_nested_parens(parenthes: str) -> List[int]:
    # Initialize the output list
    output = []

    # Define a helper function to find the level of the last non-space character
    def find_last_non_space(cur_idx):
        while cur_idx < parenthes.length and parenthes[ char at cur_idx] != ' ':
            cur_idx += 1
        return cur_idx

    # Define a helper function to find the deepest level of nesting
    def find_deepest_level(cur_idx):
        while cur_idx < parenthes.length and parenthes[char at cur_idx] != '(':
            cur_idx = find_last_non_space(cur_idx + 1)
        return cur_idx

    # Iterate over each group of parentheses
    for i in range(len(parenthes)):
        cur_idx = find_deepest_level(i)

        # If the current group is empty, add a 0 to the output list
        if parenthes[cur_idx] == '':
            output.append(0)
        # Otherwise the group, add the current level to the output list
        else:
            output.append(1 + parse_nested_parens(parenthes[cur_idx + 1:])

    return output
```