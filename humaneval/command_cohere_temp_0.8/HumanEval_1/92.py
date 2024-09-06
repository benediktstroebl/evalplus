Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses. 

The function works by using the `recursion` and `stack` modules to loop through each char in the string and differentiate between opening and closing parentheses. It checks if the current char is an opening brace, in which case it adds it to the stack, or a closing brace, in which case it checks if it matches the top of the stack. If the closing brace matches the top of the stack the brace is added to the output string and popped from the stack, if it does not it is ignored. 

The function returns a list of strings that correspond to the separate groups of parentheses.
```python
import re
from typing import List, Tuple

def separate_paren_groups(paren_string: str) -> List[str]:
    output: List[str] = []
    stack: List[Tuple[str, int]] = []
    braces = '([{'
    for brace in re.findall(braces, paren_string):
        is_open = 1 if brace == '(' or brace == '[' or brace == ' {' else -1
        stack.append((brace, is_open))
    for brace, is_open in stack:
        if is_open == 1:
            output.append(brace)
        else:
            if not stack or (stack[-1][0] != brace and stack[-1][1] == -1):
                continue
            output.append(brace)
            stack.pop()
    return output

# Tests
test_list = ['(()())', '([{}])', '( ) (( )) (( )( ))', '([{()]))']
expected_list = ['()', '[]', '()', '(()())']*4

for i in range(len(test_list)):
    assert separate_paren_groups(test_list[i]) == expected_list[i]
``` 

The tests assert that the function returns the expected output for a list of test inputs.