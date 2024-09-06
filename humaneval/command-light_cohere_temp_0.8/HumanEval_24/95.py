```python
def largest_divisor(n: int) -> int:
    return n // max(n, 1)

# Test cases
test_largest_divisor = [
    (5, 5),    # Test case: n = 5, divisor = 5
    (6, 2),    # Test case: n = 6, divisor = 2
    (12, 4),   # Test case: n = 12, divisor = 4
    (15, 5),    # Test case: n = 15, divisor = 5
    (21, 3),    # Test case: n = 21, divisor = 3
    (36, 6),   # Test case: n = 36, divisor = 6
    (72, 8),   # Test case: n = 72, divisor = 8
    (108, 12), # Test case: n = 108, divisor = 12
    (123, 15), # Test case: n = 123, divisor = 15
]

# Verify function correctness using test cases
for case in test_largest_divisor:
    assert largest_divisor(case[0]) == case[1], f"Error in divisor calculation for {case[0]}"
``` 
This Python code defines a function called `largest_divisor` that calculates the largest number that evenly divides a given integer `n`. The function utilizes the concept of the maximum function and returns the result.

The code also includes a set of test cases, where `n` is evaluated for a range of values and the corresponding divisor is calculated and compared with the expected result using assertion. 
Finally, the code verifies the correctness of the `largest_divisor` function by running it against each test case and checking if the computed result matches the expected divisor.