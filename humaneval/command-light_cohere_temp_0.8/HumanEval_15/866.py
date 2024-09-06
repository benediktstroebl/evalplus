```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test the function with different values of n
test_sequence = [10, 15, 20]
for n in test_sequence:
    actual_result = string_sequence(n)
    expected_result = f"0 {n}" * (n+1)
    print(f"Test {n}: {actual_result} (Expected: {expected_result})")
```