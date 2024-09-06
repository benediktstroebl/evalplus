Here is a Python script that includes the function `separate_paren_groups` as you described:
```python
from typing import List
def separate_paren_groups(parenthesis_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of nested parentheses and returns a list of separated parenthesis groups.
    The Each group should be balanced with all open parentheses properly closed.
    """
    Python3 syntax is used to define functions in a structured way.

# Test cases
tests = [
    ("()" , "() () ()"),
    ("()" , "()   ( )"),
    # ... other tests ...
]

# Loop through each test case
for test in tests:
    # Use string slicing to split the test string at each balanced parentheses
    group = parenthesis_string.split(braces)[1:]
    # Use the split index to find the closing parenthesis
    closing_bracket = parenthesis_string.split(braces)[0][-1]
    # Add the group and the closing parenthesis to the result list
    result.append(group + closing_bracket)

# Return the list of separated parenthesis groups
return result
```