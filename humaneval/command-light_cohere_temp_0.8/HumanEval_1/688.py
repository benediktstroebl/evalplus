```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    return [p.split('()') for p in parentheses]

def test_separate_paren_groups():
    actual_parentheses = '''( )(( ))(( )( )) )'''
    expected_results = ['()', '(())', '(()())']
    assert separate_paren_groups(actual_parentheses) == expected_results
```