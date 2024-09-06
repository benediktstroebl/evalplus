```python
def parse_nested_parens(s): 
    return [i for i, a in zip(s.split('()'), s.split('()))] if s else ''

def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((()))()')') == [2, 3, 1, 3]
```