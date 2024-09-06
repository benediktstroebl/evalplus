Here's a self-contained Python script that includes the function `separate_paren_groups` which solves the problem you described:
```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    This function takes a string containing multiple groups of parentheses and returns a list of
    separated strings.
    It sorts the individual group by balancing the parentheses and returns the content.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    for match in parentheses.split(' '('):
        result.append(match.replace('()'))
   
    balanced_out:
    return result
```
The `separate_paren_groups` function takes a string of parentheses as input and uses the `split` method to split the string into individual matches. It then uses the fact to check if the matched parentheses are balanced and if so, appends the content of the parentheses to the result list.