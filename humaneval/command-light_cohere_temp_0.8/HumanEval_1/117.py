Certainly, here's the self-contained Python script with a function that solves the problem of separating nested parentheses into individual groups, along with the corresponding tests:
```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string of parentheses as input and returns a list of the separated groups.
    >>> separated_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def open_close(match):
        return '{}{}'.format(match.group(), match.group())

    open_one = match.group()
    names = ['group{}[0]', match.group(), '{}')
    names)
    for match in open_close(s):
        if match.startswith('('(') and match.endswith ')'):
            else:
            names.append(match)

    return names
```

The provided code defines a function called `separate_paren_groups` that takes a string of parentheses as input and returns a list of separated groups of parentheses. The function uses a `open_close` helper function, which matches open parentheses and closes them with a corresponding pair of parentheses.