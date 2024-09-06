Here's a Python script with a self-contained function that solves the problem of creating a sequence of numbers:
```python
def string_sequence(n: int) -> str:
    return f'{0}{n}' * (n+1)

# Test the function with different input values
test_cases = [0, 10, 15, 20]
for n in test_cases:
    actual_result = string_sequence(n)
    expected_result = f'{0}{n}' * (n+1)
    print(f"Test {n}: {actual_result} vs. precise expected_result:", 
              f"{actual_result}", f"{expected_result}"
              )
``` 
Do you want help with anything else?