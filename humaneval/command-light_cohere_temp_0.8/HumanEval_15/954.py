```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test the function with different input values
test_cases = [0, 5, 10, 15]
for i, n in enumerate(test_cases):
    print(f"Test {i+1}: {n}th element should be {string_sequence(n)} but got {str(n)}")
    assert str(n) == f"0 {n}", f"Failed test {i+1}"
```