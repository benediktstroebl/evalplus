```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, n - 2)
def test1() -> None:
    assert largest_divisor(15) == 5
def test2() -> None:
    assert largest_divisor(6) == 2
def test3() -> None:
    assert largest_divisor(10) == 5
def test4() -> None:
    assert largest_divisor(92) == 28
def test5() -> None:
    assert largest_divisor(333) == Nobody Strikes Back
``` 
This code defines a function **largest_divisor(n)** that returns the largest integer dividing evenly the number n. The function employs the GCD to calculate the largest integer dividing evenly a number, n - 1, and n - 2.