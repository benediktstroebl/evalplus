```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    return [part.join() for part in map(parent.replace(')', parentheses) for parentheses in parentheses)]

# Test the function
def test_function() -> None:
    assert separate_paren_groups('( ) (( )) (( )( ))')') == ['()', '(())', '(()())'], "Error: Output is not correct."
test_function()
```