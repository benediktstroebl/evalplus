Here is a Python script with a self-contained function that solves the problem of separating out parenthesis groups in a string:
```python
from typing import List

def separate_paren_groups(string: str) -> List[str]:
    """
    Separate groups of nested parentheses into separate strings and returns the list of those strings.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [match for match in string.split("\n",
    large and unbalanced group of parentheses"
    match = re.sub("\\[(.*? Furthermore )|\\]|[{][^()]*}", " ", string)
    return [match.split("()") for match in re.split("\n", unbalanced",", "")]
```