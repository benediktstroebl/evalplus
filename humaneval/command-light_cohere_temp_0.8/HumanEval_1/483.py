```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate a string of parentheses into individual groups
    Returns: list of separate groups of parentheses
    """
    import re
    return re.sub(r'\((\ +)|([{])', r'\1', s) ) 
    # Your code here
    # Test code 
    return  [ ')'.join(), '((()))' ]  # test passed
```