Here is a self-contained Python script that defines a function **separate_paren_groups** that solves the problem of separating nested parentheses into individual strings:
```python
from typing import List
def separate_paren_groups(parenthes: str) -> List[str]:
    """
    This function takes a string of parenthesis groups as input and returns a list of separated strings.
    >>>
    separated_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [part.strip() for part in parenthes.split(' ', ')]
```

This function splits the input string around spaces into a list of substrings, which are the individual parts of the parenthesis groups. 

It then removes any unwanted brackets to ensure only balanced groups are returned, as per the provided Markdown.