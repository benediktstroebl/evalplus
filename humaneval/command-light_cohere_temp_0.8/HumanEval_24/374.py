```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, x)
    # Test cases
    assert largest_divisor(15) == 5
    assert largest_divisor(20) == 4
    assert largest_divisor(57) == 19
    assert largest_divisor(8) == 4
    assert largest_divisor(42) == 6
    assert largest_divisor(100) == 4
``` 
This function finds the largest number which divides a given number `n` evenly, smaller than n. It uses the formula to find the greatest number that divides evenly, then uses the Euclidean Algorithm formula for the Greatest Common Divisor to calculate the value of GCD(n - 1, x) and return the largest divisor.