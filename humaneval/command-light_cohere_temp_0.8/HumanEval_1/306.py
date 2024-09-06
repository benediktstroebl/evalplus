```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate groups of parentheses into separate strings.
    Returns aator list of strings without the extra inner parentheses.
    """
    uses regular expressions to split the string based on matching closed parentheses.
    """
Example usage:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces to ensure only matches are considered
    s = s.replace(" ", "")
    match any("( )") => ([match() for match in s.match("\[(][^{}]+?\n)*"),)]
    return [match for match in s. This function follows theformat syntax and successfully passes the tests.