```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    """
    This function splits the input string into a list of chunks,
    where each chunk is either an open parenthesis or a balanced group.
    Return a balanced groups as a list of the chunk text,
    with the chunk text itself being a balanced group of parentheses.
    """ For returned list of chunks.
    """example: ['()', '(())', '(()())']
    """
    return [chrs for chrs in input_string if chrs == '('] or [chrs for chrs in input_string if chrs == ')']
```
This code defines a function `separate_paren_groups` that takes a string as input and returns a list of balanced parenthesis groups. The function uses list comprehension to filter characters that are either '(' or the closing ')' character.