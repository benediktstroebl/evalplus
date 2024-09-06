import re
from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
    # Remove any spaces from the input string
    paren_string = re.sub(' ', '', paren_string)
    
    # Split the string into separate groups of parentheses
    paren_groups = re.findall('\\(([^()]*)\\)', paren_string)
    
    return paren_groups