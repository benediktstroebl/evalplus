Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings containing the separated parentheses:
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
            elif stack[-1] == "":
                stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group += char

    # Yield any remaining groups
    while stack:
        yield stack.pop()

# Test the function
def test_separate_paren_groups():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']
    assert separate_paren_groups("((a)(b))") == [ '((a)(b))']
    assert separate_paren_groups("(a)") == ['(a)']
    assert separate_paren_groups("()") == [()]
    assert separate_paren_groups("( a )") == ['(' + ' a ' + ')']
    assert separate_paren_groups("  (  a  )  ") == ['(' + '  a  ' + ')']

test_separate_paren_groups()
```

This script uses a stack to keep track of nested parentheses groups. It iterates through the characters of the input string, either opening or closing parentheses, or adding the character to the current group. When a closing parenthesis is encountered, the stack is checked to see if the group is nested. If the corresponding opening parenthesis is at the top of the stack, it is popped and the group is yielded. If the corresponding opening parenthesis is not at the top of the stack, it means the group is nested, so the stack is popped and the current group is yielded. Finally, any remaining groups (balanced or not) are yielded.

The `test_separate_paren_groups` function tests the `separate_paren_groups` function with various input scenarios and asserts that the output matches the expected list of strings. Each test case represents a different scenario of input parentheses, and the expected output is provided as Markdown code. The `assert` statements check that the output of `separate_paren_groups` is equal to the expected output for each test case.

This code can be executed directly and the `test_separate_paren_groups` function can be run to validate the correctness of the `separate_paren_groups` function.