Here is a self-contained Python script that solves the problem of creating a string containing space-delimited numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return f" {0:04d} ".format(n)

# Test cases
test_cases = [
    0,
    5,
    10,
    15,
    20,
]

for test_num in test_cases:
    assert string_sequence(test_num) == f" {test_num:04d} "
```
The above code defines a function string_sequence that creates a string containing the first n numbers starting from 0. It uses the string formatting to insert the numbers with leading zeros. The test_cases array is used to verify that the function is working as expected by passing different values as arguments.