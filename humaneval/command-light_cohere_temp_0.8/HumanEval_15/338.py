```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

def test_sequence(test_n: int) -> None:
    assert str(test_sequence(test_n)) == f"0 {test_n}", "Test failed"

test_sequence(0)
test_sequence(5)
```
The function 'string_sequence()' generates a string containing space-separated numbers from 0 up to the given 'n'. It uses the formula "0 n" * (n + 1)" to achieve this.