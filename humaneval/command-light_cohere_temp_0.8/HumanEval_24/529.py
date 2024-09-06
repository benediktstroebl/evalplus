```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1,  -1)
def test():
    assert largest_divisor(15) == 5
    assert largest_divisor(16) == 8
    assert largest_divisor(77) == 25
    assert largest_divisor(1095) == 50
    assert largest_divisor(0) == 0
    assert largest_divisor(-13) == -13
``` 
This Python code defines a function called `largest_divisor` that calculates the largest integer divisor of a given number `n`. The `test` function contains several assertions that check the correctness of the `largest_divisor` function by testing it with a range of values, including negative numbers.