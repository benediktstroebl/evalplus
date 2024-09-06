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
                result.append(')')
            else:
                temp_group = stack.pop()
                current_group.extend(temp_group)
                if not stack:
                    result.append(')'.join(current_group))
                    current_group = []
                else:
                    current_group = stack[-1].copy()
        else:
            current_group.append(char)
    
    if current_group:
        result.append(')'.join(current_group))
    
    return result
```

The algorithm uses a stack to keep track of open parentheses and a list to store the current string of parentheses. When it encounters a closing parenthesis, it checks if it matches the most recent open parenthesis. If it does not, it assumes the closing parenthesis belongs to the next outer pair, and therefore, the stack item is appended to the current string and the stack is popped. If it matches the most recent open parenthesis, the stack is popped and the parentheses are considered paired and not added to the result. The result list is then returned. 

This approach does not require removing spaces from the input string, as specified in the problem statement, making the code more concise and efficient. 

The unit test based on the provided test case can be added, as you have requested. 
```python
test_string = '( ) (( )) (( )( ))'
expected_result = ['()', '(())', '(()())']

self.assertEqual(expected_result, separate_paren_groups(test_string))
```

This test case will ensure that the function `separate_paren_groups` produces the desired output. 

To run this test, you can add this code to the same file as the `separate_paren_groups` function and invoke the testing functionality depending on the testing framework you are using. 

For example, if you are using pytest, you can add an appropriate decorator to the test function at the top of the file and execute the tests using `pytest filename.py`.