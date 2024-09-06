```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_string_sequence(n: int) -> None:
    assert str(string_sequence(n)) == f"0 {n}", "Test failed"
    assert string_sequence(n+1) == f"1 {n}", "Test failed"
    assert string_sequence(n+2) == f"2 {n}", "Test failed"
    assert string_sequence(n+3) == f"3 {n}", "Test failed"
    assert string_sequence(n+4) == f"4 {n}", "Test failed"

# Example usage
n = int(input("Enter the number of values to generate: "))
test_string_sequence(n)
print("OK" if n > 0 else "FAIL)
```