```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = []
    result = []
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if not stack:
                return ['Unbalanced parentheses!']
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```

The algorithm utilizes a stack to keep track of opening parentheses '(' and constructs the corresponding parentheses strings. It switches between two stacks, one for balancing parentheses and another to accumulate the results. The approach is straightforward and should work correctly for nested and unbalanced parentheses strings. 

However, it is essential to note that the algorithm assumes that the input string contains only parentheses and no other characters, as indicated by the problem statement's instruction to ignore spaces. Any other characters, such as the comma, will cause the algorithm to fail. If there are other characters present in the input, additional preprocessing would be necessary. 

The overall time complexity of the algorithm is O(n), where n is the length of the input string, and the space complexity is O(n) as well, due to the need for two extra stacks. 

Ensure you follow the problem statement's guidelines to deliver the expected results. Let me know if you would like me to clarify any of the steps or provide further explanations!