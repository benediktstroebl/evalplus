```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    nest = []
    for c in s:
        if c == '(':
            stack.append(nest.append(1))
            nest = []
        elif c == ')':
            stack.pop()
            if stack:
                nest.append(stack[-1])
            stack = []
    return nest
# Example usage
test_cases = [
    ("(())",
    ("()()()"),
    ("()()()()"),
    ("(()()())()()",
]

for test_case in test_cases:
    nest = parse_nested_parens(test_case)
    if nest != [2, 3, 1, 3]:
        print(f"Error in test case: {nest}")
```
The provided Python code defines a function `parse_nested_parens` that parses and returns the deepest level of nesting for a given input string containing multiple groups of parentheses separated by spaces. 

It employs a stack to keep track of opening parentheses and a nested list to store the results of nested parentheses. 

The code iterates through the input string, and for each character, it decides whether to push the current character onto the stack (indicating an opening parent) or pop the top element from the stack (indicating a closing parent). 
Additionally, the code provides a series of test cases to validate the function's behavior.