Here is a Python script that contains a self-contained function that solves the problem:
```python
def string_sequence(n: int) -> str:
    return f" {0:02} ".join(range(n))

# Test the function with different input values
for i in range(1, 6):
    assert string_sequence(i) == f" {i:02} ", f"Wrong sequence: {i:02} != {str}"
```

This script defines a function that generates a string containing space-separated numbers from 0 up to a given input 'n'. The generated sequence is then passed through the test using the `assert` statement, which verifies if the generated sequence matches the expected output for the given input.