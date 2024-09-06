```python
def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string of nested parentheses.
    Returns a nested list of the levels of nesting of parentheses.
    """
    = [
        [2, 3, 1, 4], [3, 2, 1, 4]]
    """
    return [match[1::2] for match in [match.match(r'(((.),?In)), 0, ((),()))
    for match in s.match(r'((.),()))]]
```