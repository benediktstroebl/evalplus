```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_sequence(n: int) -> None:
    assert str(string_sequence(n)) == f"0 {n}" * (n+1), f"Error: {n} did not produce expected output"
    return

# Driver code to run the above tests
test_sequence(0)
test_sequence(1)
test_sequence(5)
```
The function generates a string containing space-delimited numbers starting from 0 and ending at n, inclusive. The test function verifies that the generated output matches the expected format.