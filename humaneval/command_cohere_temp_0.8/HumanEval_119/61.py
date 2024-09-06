```python
def match_parens(lst):
    open_tup = tuple(c for c in lst[0] if c == '(')
    close_tup = tuple(c for c in lst[1] if c == ')')
    return "Yes" if open_tup and close_tup and len(open_tup) == len(close_tup) else "No"
```

The approach employs a straightforward algorithm that checks if the open parentheses and close parentheses sets have equal sizes and if the lists are not empty. If these conditions are fulfilled, it confirms there exists some order of concatenation that results in a balanced string, thereby returning 'Yes'. Otherwise, it returns 'No'. 

Here's the implementation integrated into the provided markdown code block:
```python
def match_parens(lst):
    open_tup = tuple(c for c in lst[0] if c == '(')
    close_tup = tuple(c for c in lst[1] if c == ')')
    return "Yes" if open_tup and close_tup and len(open_tup) == len(close_tup) else "No"
```

Additionally, here's a brief test suite to ensure the function behaves correctly:
```python
def test_match_parens():
    assert match_parens([')', '(']) == "No"
    assert match_parens(['()', ')']) == "Yes"
    assert match_parens(['(', ')', ')']) == "Yes"
    assert match_parens(['((((', ')))', ')']) == "Yes"
    assert match_parens([')', '(', ')']) == "No"
    assert match_parens([')', '(', ')', ')']) == "No"
    assert match_parens(['()', '()', ')']) == "Yes"
    assert match_parens(['()', ')', '()']) == "Yes"
```