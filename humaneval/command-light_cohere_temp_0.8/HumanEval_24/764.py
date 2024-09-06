```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if all(d%i == 0 for i in range(1, n)))
def test1():
    assert largest_divisor(15) == 5
def test2():
    assert largest_divisor(10) == 5
def test3():
    assert largest_divisor(16) == 4
def test4():
    assert largest_divisor(14) == 2
``` 
This Python script defines a function `largest_divisor` that finds the largest integer divisor for a given number `n`. It utilizes a generator expression and the `all` function to check if all divisors of `n` are equal to zero, and returns the largest such divisor. 

This script also includes several tests to verify the correctness of the `largest_divisor` function.