```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if not stack:
                yield current_group
            elif stack[-1] == current_group:
                stack.pop()
                current_group = stack.pop() if stack else ""
            else:
                current_group = stack.pop()
    else:
        yield current_group
```

This code defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of nested pairs of parentheses, ignoring any spaces. The function iterates through the input string. When it encounters an open parenthesis `(`, it pushes the current group (built so far) to a stack and starts a new group. When it encounters a closing parenthesis `)`, it checks whether the stack is empty. If yes, it yields the current group. If no, it checks if the top of the stack matches with the current group. If they match, it pops them from the stack, and continues building the current group with the popped group. If they don't match, it only pops the top of the stack to continue building the current group from scratch. The resulting list of groups is returned. 

This solution assumes that the input string contains only parentheses and spaces, and it handles the nesting of parentheses correctly. It also does not require any additional libraries beyond the Python standard library. 

```python
```

This script can be executed by placing it in a Python environment and running it with the command `python -i script_name.py` to execute the code interactively, or `script_name.py` to execute the code without interactive input. 

To test this script, you can create a file called `test_separate_paren_groups.py` in the same directory as the script, and copy the following code into it:
```python
def test_separate_paren_groups():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']
    assert separate_paren_groups("((a)(b))") == [ '((a)(b))']
    assert separate_paren_groups("(a)") == [ '(' + 'a' + ')' ]
    assert separate_paren_groups("())") == [ '(())' ]
    assert separate_paren_groups("( a )") == ['( a )']
    assert separate_paren_groups("(  a  )") == ['(  a  )']
    assert separate_paren_groups("(a  b)") == ['(' + 'a' + '  ' + 'b' + ')' ]
test_separate_paren_groups()
```

This test script includes several test cases to validate the behavior of the `separate_paren_groups` function against expected outputs. 

To run the test script, you can use the command `python -i test_separate_paren_groups.py` to execute the code interactively, or `test_separate_paren_groups.py` to execute the code without interactive input. 

Please note that you should place the script and test script in the same directory to avoid directory errors.