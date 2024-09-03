```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string of nested parentheses separated by spaces as input and returns the deepest level of nesting.
    Input:
    s (string of parentheses)
    Output: list of deepest level of nesting, or an empty list if no nesting
    """
    # set up some test cases
    test_cases = [
        "(()()) ((())) () ((())()())",
        "(((((())))))",
        "(((((((()))))))))",
        "()()()()()()()()()()()",
        "() ((())()) ",
        "() (()) ()"
    ]
    # create a list of the results
    results = []
    # loop through the test cases
    for test in test_cases:
        # split the test into a list of parentheses
        parList = test.split('()
        spaces=' ')
        # parse the list of parentheses
        lst = [int(x) for x in parList]
        # add the list of integers to the results list
        results.append(lst)
    # add the test case to the list
    return results
```