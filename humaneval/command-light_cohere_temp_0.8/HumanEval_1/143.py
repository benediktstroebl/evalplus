```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """ Separate groups of parentheses into separate strings.
    - Returns balanced (each open brace is properly closed) and not nested within each other
    - ignores spaces
    - Returns list of strings
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [pa for pa in s.replace(")" in pa) if pa != "" and not pa.isdigit()]
 could be improved?  # https is always empty.  # better would would example a sequence of balanced parentheses.  # good practice is easy to implement  # and can make it a bit faster than the original.  # approach.  # Add's information in parentheses.  # it's a backtracking.  # loop will not back.  # along the boats.  # information,  # input.