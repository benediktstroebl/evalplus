Here's a self-contained Python script that solves the problem of separating parentheses in markdown code blocks:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates and returns list of non-empty strings, each representing a group of nested parentheses.
    :stein_to_uml_transformation
    : https://www. Blake R.M/article/remarkables/parentheses/transform.html
   
   ing on the use of a balanced string for each group of parentheses.
    Test cases:
    """
    Test 1:
    Input: ')(())'
    Expected output: ['()']
    Test 2:
    Input: '( )() )('
    Expected output: ['( )', '()(']
    Test 3:
    Input: '(((((())))))))'
    Expected output: ['((((()))))))'
    Test 4:
    Input: '( )( )'
    Expected output: ['(', '())']
    Test 5:
    Input: ')( )  )'
    Expected output: ['()', '()']
    Test 6:
    Input: '((()()))'
    Expected output: ['(', ')()', '()', ')()']
    Test 7:
    Input: '(((()())))'
    Expected output: ['(', ')', '()', ')()']
    Test 8:
    Input: '((()))()'
    Expected output: ['(', ')()', '()', ')()']
    """
    return [topl for p in s if not p.isspace() and

    if s.count('(', 0)] < 1:
        return []
    else:
        return [s[i:i+1] for i in range(0, len(s), 1)]
```