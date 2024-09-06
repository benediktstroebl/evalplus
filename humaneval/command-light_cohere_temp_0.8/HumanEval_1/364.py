```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [p.join(')', s) for p in '()'*6]

# Test cases
tests = [
    'Input: ( )(())'
    'Output: ()'
    '''
    'Input: (()) )()()'
    'Output: (())'
    '''
    'Input: (( (( ) ) ))'
    'Output: ((()))'
    '''
]

# Function Call
for test in tests:
    print(separate_paren_groups(test))
``` 
This code defines a function called `separate_paren_groups` that takes a string `s` as input and returns a list of substrings separated by parentheses. The function uses a nested loop and the pattern `'()'`*6 to capture each group of parentheses and returns the list of those groups. The test cases define a expected output for different input strings, and the function is called with various input strings, and its output is printed to verify its correctness.