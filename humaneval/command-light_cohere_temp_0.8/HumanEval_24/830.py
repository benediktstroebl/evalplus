```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, n - 2)
def test1() -> None:
    assert largest_divisor(15) == 5
def test2() -> None:
    assert largest_divisor(6) == 2
def test3() -> None:
    assert largest_divisor(10) == 2
def test4() -> None:
    assert largest_divisor(16) == 4
def test5() -> None:
    assert largest_divisor(12) == 4
def test6() -> None:
    assert largest_divisor(8) == 4
def test7() -> None:
    assert largest_divisor(42) == 6
def test8() -> None:
    assert largest_divisor(9) == 3
```
The provided Python script contains a function `largest_divisor` that calculates the largest number which divides a given number evenly, smaller than the input number. The function uses the `gcd` to calculate the greatest common divisor of the input numbers minus 1 and n - 2, which is the guarantee to be a divisor of the number n. The function also includes several test cases to validate its behavior.