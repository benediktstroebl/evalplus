```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test the function with different inputs
test_cases = [0, 1, 10, 123, 12340]
test_results = [string_sequence(x) for x in test_cases]

print("Test Results:")
for res in test_results:
    print(res, end=' ')
```