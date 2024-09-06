Here is a Python script that defines a function that generates a string of numbers from 0 up to the provided n:
```python
def string_sequence(n: int) -> str:
    return " ".join([str(i) for i in range(n)])

# Test cases
test_cases = [
    (0, '0'),
    (5, '0 5'),
    (10, '0 9 10 11 12 13 14'),
    (1, '1'),
    (201, '201 201 202 203 204 205'),
]

for n, expected in test_cases:
    actual = string_sequence(n)
    print(f"Test case {n}: {actual} -> {expected}")
``` 
This code provides a self-contained function and test cases to solve the problem.