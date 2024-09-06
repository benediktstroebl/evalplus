Here is a self-contained Python script that defines a function string_sequence, which generates a string containing space-delimited numbers starting from 0 up to the provided n:
```python
def string_sequence(n: int) -> str:
    return " ".join([str(i) for i in range(n)])

# Test cases
test_cases = [
    (0, '0'),
    (5, '0 1 2 3 4 5'),
    (10, '0 10 20 30'),
    (100000, '1000000 100000')
]

for case in test_cases:
    assert case[0] == case[1], "Test case {} failed".
``` 
This script provides a simple and self-contained solution to the problem you have mentioned.  It can be used as a starting point to build upon with more complex implementations.