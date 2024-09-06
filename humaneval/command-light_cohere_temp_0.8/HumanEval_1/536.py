```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    return [p.join(')', '()') for p in parentheses]

def test_separate_paren():
    assert separate_paren_groups([r'(x) for x in 'test']) == ['(', '())', '()()', '()()']
``` 
This code has a function **separate_paren_groups** that takes a list of strings as input and returns a new list with each balanced pair of parentheses as a string. The test_separate_paren function tests the correctness of the **separate_paren_groups** function by asserting that the result of the function call with the test input is correct.