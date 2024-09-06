```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3} {n+4}"

# Test cases
def test_sequence(test_case: str) -> None:
    assert len(test_case) == 5
    assert test_case[0] == '0'
    assert test_case[-1] == '1'
    assert test_case[-2] == '2'
    assert test_case[-3] == '3'
    assert test_case[-4] == '4'

test_sequence('Test Case 1')
test_sequence('Input: 0,1,2,3,4')
```