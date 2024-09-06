```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}"*len(str(n))
    
# Test case 1
def test_string_sequence(test_case: int) -> None:
    assert string_sequence(test_case) == f"0 {test_case}*len(str(test_case))", "Pass test 1 failed"

# Test case 2
test_string_sequence(5)
```