```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, int('inf')) + 1
 
def test1():
    assert largest_divisor(15) == 5
def test2():
    assert largest_divisor(6) == 2
def test3():
    assert largest_divisor(100) == 4
def test4():
    assert largest_divisor(0) == 0
def test5():
    assert largest_divisor(-10) == -1
``` 
The provided Python script defines a function called `largest_divisor` that calculates the largest divisor of a given number `n`. The function uses the `gcd` function from the math library to find the greatest number that divides evenly into `n - 1` and then adds 1 to this result. The script also includes several test cases that verify the correctness of the `largest_divisor` function for different input values.