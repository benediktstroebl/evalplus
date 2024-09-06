```python
def parse_nested_parens(s):
    return [i for i, group in enumerate(s.parse_group(s), groups=[g.pop(). start=True if g in ['()', '(', '[]', ')'] for g in groups]))

def parse_group(s):
    return s.replace(). string.split(' ',s)
 return [g.pop(i,s) for i in range(0, len(s), -1)] if s and any(g for g in ['()', '(', '[]', ')'])

# tests
parse_nested_parens('(()()) ((())) () ((())()())')')
```
This code provides a function `parse_nested_parens` that accepts a string as its parameter. The string is expected to contain multiple groups of nested parentheses separated by spaces. The function uses a nested list comprehension and the `pop()` function to traverse the string and identify each group of parentheses. It returns a nested list of integers starting from the deepest level of nesting.

The code also provides a `parse_group` function that accepts a string and uses the same logic to parse the nested parentheses.