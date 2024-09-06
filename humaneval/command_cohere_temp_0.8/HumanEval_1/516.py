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
                return []
            current_group += stack.pop()
        else:
            current_group += char

    return [group for group in stack if group]
```
This Python script takes a string as input and returns a list of strings. Each string in the list represents a balanced group of parentheses found in the input string. The algorithm works by using a stack to keep track of open parentheses '(' and building the current group when encountering closing parentheses ')' and other characters. Finally, it returns the stack elements themselves, if any, which correspond to the separate groups of parentheses. 

Below is a simple test case to verify the functionality of the script:
```python
test_case = '( ) (( )) (( )( ))'
expected_result = ['()', '(())', '(()())']

print(f'\nTest case:\n{test_case}\n')
print(f'Expected result:\n{expected_result}\n')

assert separate_paren_groups(test_case) == expected_result
```
The provided test case and expected result illustrate the functioning of the script. The input string `test_case` contains different groups of parentheses, and the expected result `expected_result` should retrieve the balanced groups correctly.  This python script is a simple and efficient way to parse different groups of parentheses.  It can be used as a basic building block for various applications that require parsing and manipulating text.