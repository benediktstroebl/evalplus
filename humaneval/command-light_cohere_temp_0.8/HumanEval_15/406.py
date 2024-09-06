Here's the code:
```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_sequence(n):
    assert len(string_sequence(n)) == n+1
    assert string_sequence(n).string() == f"0 {n}"*n
    assert string_sequence(n+1) == f"1 {n}1"* (n+2)
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 105'
    assert string_sequence(10) == '0 1020'
```
This script defines a function **string_sequence** that generates a string containing space-delimited numbers starting from 0 up to the given integer **n**. It also includes a test function **test_sequence** with several assertions to validate the function's output for different input values.