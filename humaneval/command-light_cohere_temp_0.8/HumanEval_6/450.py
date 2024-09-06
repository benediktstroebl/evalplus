```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string of nested parentheses as input and returns a list of their deepest nested levels.

    Test cases are
    following:
    - Test case 1: ((()))
    - Test case 2: (())()
    - Test case 3: ((())()())
    - Test case 4: ())
    - Test case 5: ((()))(()())

    Input: 

    Output: [3, 2, 1]
    """
    output = []
    for match in s.format(s, '()'):
        if match == '(':
            output.append(len(output))
        else:
            output.append(match)
    return output
 ```