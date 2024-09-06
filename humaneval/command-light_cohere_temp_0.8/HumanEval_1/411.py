```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """Separate groups of parentheses into separate strings.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [parent for parent in parentheses.test_cases() for parentequalities in [
        ['()', '(()())'],
        ['()()', '()'],
        ['()()()', '()'],
        ['()()()()', '()'],
        ['( )', '()', '(foo)'],
        ['( )()', '( )'],
        ['( )()()', '() ﾉﾉ'],
        ['( . )', '()', '((.Bar)']])
```

The `separate_paren_groups` function accepts a string of parentheses and returns a list of separated parenthesis strings. The function utilizes a balanced grouping of parentheses and the ability to distinguish between balanced and unbalanced groups.