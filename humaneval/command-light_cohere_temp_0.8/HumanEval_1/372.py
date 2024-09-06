```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates balanced parentheses from the input string and returns the list of separate strings.
    >>> ['()', '(()())']
    """
    stack = []
    for char in s:
        if char == '(': stack.append(char)
        if char == ')':
            if stack:
                open_paren = stack.pop()
                return open_paren + ')'
    return list(stack)

#Test cases
tests = [
    "Input: '() (( )) (( )( ))'
    Output: ['()', '(()())']
    
    "Input: ((()))"
    Output: ['()', '')
    
    "Input: (( ) ) (())"
    Output: ['(', ')', '())']
    
    "Input: (( () ))"
    Output: ['(', '())']
    
    # Complex case
    "Input: ( () ( ) ) ( )"
    Output: ['(', '())', '(', '())']
]

for test_case in tests:
    actual_output = separate_paren_groups(test_case)
    print(f'Expected: {', ', '.join(actual_output))
``` 
This code defines a function `separate_paren_groups` that separates balanced parentheses from an input string and returns a list of separate strings. It then defines a test cases, and the function is run with each test case. The expected output is printed alongside the actual output.