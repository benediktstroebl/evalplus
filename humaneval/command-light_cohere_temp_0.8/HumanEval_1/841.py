```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    This function splits a string of parenthesis groups into individual strings.
    Returns a important list of those strings.
    """
    balanced (each open brace is properly closed) and not nested within each other
    """
    return [environ[0] for environ in zip('('(' + parenthesis + ')' for parenthesis in parentheses.  )]
def test_function(test_string: str) -> None:
    """
    Test suite function.
    Tests the primary a string of balanced parentheses.
```
And here's the test cases:
```python
def test_cases():
    return [
        "(")()".test(),
        "()(())",
        "()()()",
        "() ()",
        "((())) ((()))",
        "() () ()",
        "()() (( ))"
    ]
test_cases()
```