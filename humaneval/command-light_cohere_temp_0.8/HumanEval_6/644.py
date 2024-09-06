```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    Parses a string containing multiple groups of nested parentheses separated by spaces.
    Args: 
        - parent_string (str): string representing multiple groups for nested parentheses separated by spaces
    Returns: 
        - list[int]: a list of deepest levels of nesting for each group of parentheses
    """
    return [match.group().count for match,group in re.count() for match in paren[0] for paren in paren.group in string.use(match.group.match)]
 for re.match() that looks for a match of a group of parentheses in the parent_string. The match.string.parent_string. If the match is a count(): a list of groups in the parent_string. The count is done by using the match. A match object for re.match() that looks for a match of a group of parentheses in the parent_string. If there are no matches, an empty list is returned.
```