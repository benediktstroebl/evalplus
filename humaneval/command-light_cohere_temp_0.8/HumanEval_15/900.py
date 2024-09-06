Here is a Python script with a self-contained function that solves the problem of generating a string of space-separated numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return " ".join(str(i) for i in range(n))

# Test cases
test_cases = [
    0, 
    5, 
    10, 
    15, 
    20, 
    25, 
    30, 
    35, 
    40, 
    45, 
    50
]

for i, n in enumerate(test_cases):
    actual_result = string_sequence(n)
    expected_result = str(test_cases[i])
    assert actual_result == expected_result, f"Test {i+1}: {actual_result}"
```