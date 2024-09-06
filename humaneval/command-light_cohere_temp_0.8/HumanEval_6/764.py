```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function aims to parse a string of nested parentheses.

    Args:
        s (str): string to parse

    Returns:
        list of the deepest level of nesting, or an empty list if parsing fails
    """
    import re
    pattern = r'\((\d*)\)+'
    caps = re.compile(pattern, s)
    return [int(c) for c in caps] if caps else []

#Test cases
test_str = '(()()) ((())) () ((()))'
test_list = parse_nested_parens(test_str)
print(test_list)
test_fail = parse_nested_parens('foo')
print(test_fail)
```