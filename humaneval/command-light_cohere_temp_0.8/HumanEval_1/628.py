Here is a self-contained Python script that solves the problem of separating parentheses:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [parent for parent in s.group(p) for p in s.group(p].format('()')]
# Test case
tests = '''( ) (( )) (( )( ))''''
# Test cases
tests_cases = [test.assertEqual('list([
    separate_paren_groups(s) for s in tests]))
# Assertions
assert len(tests_cases) == 4, "Test cases have incorrect length"
assert tests_cases[0] == ['()'], "First test returned unexpected value"
assert tests_cases[1] == '(()')', "Second test returned unexpected value"
assert tests_cases[2] == '(()())', "Third test returned unexpected value"
assert tests_cases[3] == '()', "Fourth test returned unexpected value"
```
This code defines a function called `separate_paren_groups` that takes a string `s` as input and returns a list of parenthesis groups. The function works by iterating over the groups of parentheses in the string, using the `group()` method to split the string into groups. The `format()` method is used to remove any additional parentheses. The test case and test cases are defined to ensure that the `separate_paren_groups` function works correctly for a variety of inputs.