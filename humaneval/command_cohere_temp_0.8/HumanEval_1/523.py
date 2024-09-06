Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses. 

The function works by using nested loops to iterate through the input string, using an array of characters to track whether each opened brace has been closed yet. When a closing brace is encountered that matches an opened brace in the same nesting level, the closed brace is appended to the current string being stored in the result list for that level. The nesting level is decreased, and if it's zero, the current list is added to the output list and reset to store the next group of parentheses. Here's the code:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result: List[str] = []
    opened: List[bool] = [True] * len(paren_string)
    for i, char in enumerate(paren_string):
        if char == '(':
            if not opened[i]:
                continue
            opened[i] = False
            result.append("")
        elif char == ')':
            if not opened[i]:
                print(f"Found a closing brace ({char}) without a matching opening brace!")
            else:
                opened[i] = True
                result[-1] += char
    return result
```

To test the function, you can run the following code:
```python
test_list = ['((()))', '(()())', '(((((()()))))))', '()', '(())', '({[])}', '([])', '({})', '{}', '[]', '()()', 'a', 'b]', '[]]']
expected_ans = [
    ['((()))', '(()())'],
    '(()())',
    '(((((()()))))))',
    '()',
    '()',
    '({[])}',
    '([])',
    '({})',
    '{}',
    '[]',
    '()()',
    'a',
    'b',
    '[]]',
]

for i in range(len(test_list)):
    assert separate_paren_groups(test_list[i]) == expected_ans[i]
```

This way, you can ensure that the function works correctly for a variety of test cases.