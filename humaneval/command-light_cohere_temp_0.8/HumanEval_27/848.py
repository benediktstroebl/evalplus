```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isupper() else lowercase() else c.isupper() for c else c.islower() if c)
```

def test_flip_case():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('world') == 'udrowO'
    assert flip_case('  hello world  ') == 'ohell world'
```  The provided function, flip_case, takes a string as input and applies the specified case transformation. It iterates through specific tests to ensure that the function behaves correctly.