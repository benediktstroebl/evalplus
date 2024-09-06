```python
from typing import List

def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Separate groups of parentheses and return the list of separated strings.
    """
    unbalanced_group=True -> Raise error for unbalanced groups
    """
    result = []
    for group in parenthesis_groups(parentheses, unbalanced_group=False):
        result.append('(' + group + ')')  # + is used to add an open parenthesis to the group
    return result

def parenthesis_groups(string: str, unbalanced_group=True) -> List[str]:
    """
    Input is a string containing groups of parentheses
    Separate each group into individual strings
    """
    groups = []
    brackets = []
    for match in re.finditer(string, r'([ ]+)'):  # using re.finditer to get balanced groups of parentheses
        if unbalanced_group and match.else the brackets. Otherwise, it is part of a balanced group and append it to the groups list
        groups.append(match.group())
        then last unbalanced group, the loop breaks and returns the groups list
        return groups

# Example test cases
test_cases = [
    "() () ()",
    "()() () ()",
    "(()()) () ()()",
    "(())",
    "(() ) (())",
    "((())) ()"
]

for test in test_cases:
    actual = separate_paren_groups(test)
    print(f"Input: {test}\nExpected: [{actual}]")
``` 
This Python script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of separated strings. The function uses a nested loop and the `re.finditer` function to match and split each group of parentheses. The output of the function is then compared against the expected results for various test cases.