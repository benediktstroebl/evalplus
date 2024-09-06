```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [p.strip() for p in s. for _ in ['()', '(', ')']]

# Test
def test_case() -> None:
    return separate_paren_groups('( ) (( )) (( )( ))')') == ['()', '(())', '(()())']
test_case()
``` 
This Python code defines a function `separate_paren_groups` that takes a string as input and returns a list of parenthesis-grouped strings. The function uses a strings that match either '(' or ')', and then extracts the inner string using a generator expression, effectively separating the parenthesis groups. The test_case function is provided to verify that the `separate_paren_groups` function behaves as expected and returns the correct result for the given input string.