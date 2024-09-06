```python
def flip_case(string: str) -> str:
    return ''.join() if not string else string.flip()
 # For a string that contains only lowercase letters, return the original string.

# Tests
def test_flip_case():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('123')] == '123')
    assert flip_case('abc123') == 'cAB123'
    assert flip_case('ÄöÜ') == 'öÜ'
```