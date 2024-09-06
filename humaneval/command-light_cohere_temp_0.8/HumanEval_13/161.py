```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    return max(a, b) / gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(10, 5) == 5
    assert greatest_common_divisor(8, 10) == 2
    assert greatest_common_divisor(48, 72) == 24
    assert greatest_common_divisor(27, 54) == 27
    assert greatest_common_divisor(3, 3) == 3
    assert greatest_common_divisor(2, 7) == 7
```
The above code defines a function `greatest_common_divisor` that computes the greatest common divisor of two integers using the `gcd` function, which calculates the greatest common divisor of the two numbers. The `gcd` function returns the for a given pair of integers, while the `greatest_common_divisor` function returns the result.

The `main` block is used to run the test of the `greatest_common_divisor` function with a variety of input pairs. The assert statements are used to check that the function is returning the correct results for the given input pairs.