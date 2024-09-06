```python
def parse_nested_parens(s: str) -> List[int]:
    levels = []
    for match in s.match(r'(([^))'):  # Matches the deepest level of nesting
        levels.append(match.group().  #match.groupindex: int)
         # Index of the current opening parenthesis
        groups = match.group('('()')).  # Matches the match parenthesis groups
        levels += groups
    return levels

```
Do you have a handy function that uses the `re` module's `match()` function to parse and return the deepest level of nesting for each set of parentheses in the input string.