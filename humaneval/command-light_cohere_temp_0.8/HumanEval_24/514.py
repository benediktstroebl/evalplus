```python
def largest_divisor(n: int) -> int:
    return (n-1) // gcd(n-1, 1)
def test_largest_divisor(test_num: int) -> None:
    assert largest_divisor(test_num) == test_num // 1
    
# Example usage 
test_largest_divisor(15)
``` 
This Python script defines a function `largest_divisor` that finds the largest integer divisor of a given number `n` under the assumption that the divisor must be less than `n`. It also includes a `test_largest_divisor` function that provides a test case for the `largest_divisor` function, asserting that it returns the correct result for the given input.