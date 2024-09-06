```python
def largest_divisor(n: int) -> int:
    return (n-1) // gcd(n-1)

def gcd(x: int, y: int) -> int:
    while y != 0:
        x, y = y, x % y
    return x

if __name__ == "__main__":
    assert largest_divisor(15) == 5
    assert largest_divisor(9) == 3
    assert largest_divisor(24) == 8
    assert largest_divisor(0) == 0
    assert largest_divisor(4) == 4
``` 
This script defines a function `largest_divisor` that calculates the largest integer that evenly divides a given number `n`. It also defines a helper function `gcd` to calculate the greatest common divisor of two numbers. The script then includes several test cases to validate the correctness of the function.