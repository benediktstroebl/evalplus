```python
def parse_nested_parens(s): 
    return [i for i, group in enumerate(s.group(match(r'([)(]+)\)', re.sub(r'()*', '', group))) if len(group) > 1]

def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())')') == [2, 3, 1, 3]
```