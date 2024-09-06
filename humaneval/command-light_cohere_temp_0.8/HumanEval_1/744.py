Here is a Python script with a self-contained function that solves the problem of separating different groups of parentheses:
```python
from typing import List

def separate_paren_groups(string: str) -> List[str]:
    """
    Separate balanced parentheses groups into a list.

    Returns: list of non-empty strings, each containing balanced parentheses.
    """
    take care of each level of grouping, whether it is a set of open parentheses or a set of closed parentheses, 

    balance each group using the stack-effect (add open parentheses, then multiply by closed ones) and then
    add closed ones to the front of the stack until balanced.
    Returns a a list of strings containing balanced groups of parentheses.
 :param string (str): The input string to split into balanced groups of parentheses
 :return: A list of non-empty strings, each balanced group of parentheses

Example:
```python
print(separate_paren_groups('( ) (( )) (( )( ))'
['()', '(())', '(()())', '()'])
```