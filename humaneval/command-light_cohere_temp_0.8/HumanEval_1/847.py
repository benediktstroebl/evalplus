Certainly! Here is the self-contained Python script with a self-contained function that solves the problem of separating nested parentheses:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of balanced parentheses from the input string.
    Returns ans of balanced parentheses as separate strings.
    """
    balanced:
        [(), ()],
        ((),())
    """
    return [match.group(i) for i, match in re.org_match(s, r"\([([\{\[]\}])\])").split()]

# Test the function
def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))')') == ['()', '(())', '(()())']

# Run the test function
test_separate_paren_groups()
```
This code defines a function called `separate_paren_groups` which takes a string as input and splits it into separate groups of balanced parentheses, which can be nested or not. The function returns a array of these groups. The `test_separate_paren_groups` function is used to test the `separate_paren_groups` function with an example string, and ensures that the output is correct. 

Note: this is a self-contained implementation and does not require any external modules or functions.