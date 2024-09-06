Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of separate groups of parentheses. The code is formatted with Markdown code blocks to present the problem statement and the solution, as requested:
```python
# Markdown code block: Input
from typing import List

# Markdown code block: Function description
def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. 
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    
    """
    # Split the input string into a list of characters
    char_list = list(paren_string)
    # Use a stack to keep track of open parentheses
    stack = []
    # Use a result list to store our final answers
    results = []
    # Iterate through each character in the input string
    for char in char_list:
        # If the current character is an open parenthesis, add it to the stack
        if char == '(':
            stack.append(char)
        # If the current character is a close parenthesis, check if it matches the top of the stack
        elif char == ')':
            # If the stack is empty, this close parenthesis is invalid, ignore it (and all subsequent close parentheses)
            if not stack:
                break
            # If the current close parenthesis matches the top of the stack, remove the open parenthesis and add the current string to results
            if char == stack.pop():
                results.append(str())
            # If the current close parenthesis does not match the top of the stack, add the open parenthesis back to the stack
            else:
                stack.append(char)
    # If the stack is not empty at the end, that means there are unbalanced parentheses, and we only output valid results
    if stack:
        results = []
    # Return the results
    return results

# Markdown code block: Test Cases
# Test case 1
paren_string = '('
expected_result = [paren_string]

# Test case 2
paren_string = '(()'
expected_result = [('('), '()']

# Test case 3
paren_string = '()'
expected_result = [('()')]

# Test case 4
paren_string = '((('
expected_result = ['(((']

# Test case 5
paren_string = '( ) (( )) (( )( ))'
expected_result = [('('), '()', '(())', '(()())']

# Test case 6
paren_string = '  (  )  '
expected_result = ['()']

# Actual tests
for paren_string, expected_result in [
    ('(', ['(']),
    '(()', ['(' , '()']),
    '()', [('()')],
    '(((', ['((('],
    '( ) (( )) (( )( ))', ['(', '()', '(())', '(()())'],
    '  (  )  ', ['()'],
]:
    assert separate_paren_groups(paren_string) == expected_result, "Failed on {}".format(paren_string)
```

This code contains a brief description of the function, the function itself, and test cases to validate its correctness. The function uses a stack to keep track of open parentheses and iterates through the characters of the input string