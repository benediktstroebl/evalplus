```python
def separate_paren_groups(s: str) -> List[str]:
    return [parent for parent in s.group() for parent in [')'.split('(') + ')', 1)[0]

# tests
def test_separate_paren():
    assert separate_paren_groups('( ) (( )) (( )( ))')') == ['()', '(())', '(()())']
```