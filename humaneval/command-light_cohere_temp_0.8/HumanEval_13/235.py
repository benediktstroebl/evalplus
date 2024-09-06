```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one input is required.")
    return max((d for d in range(1, max(a, b)) if a % d == 0 and b % d == 0))
def test_gcd():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
def test_gcd_error():
    try:
        greatest_common_divisor(0, 5)  # zero divided by anything is always 0
    except ValueError as e:
        print(f"Error: {e}")
```
The provided code includes a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. The function first checks if either input is empty, and if so, raises a `ValueError`. The code also includes two test cases: `test_gcd` with passes the test for the function, and `test_gcd_error` to handle a potential division by zero exception. 
Note that the code is self-contained and does not require any external variables or functions for proper execution.