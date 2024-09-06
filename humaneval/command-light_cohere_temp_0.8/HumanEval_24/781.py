```python
def largest_divisor(n: int) -> int:
    """Finds the largest integer which divides the given number evenly, smaller than n"""  
    # Using divisibility by primality and factoring
    factor = [x for x in range(1, n+1) if n % x == 0]
    lcm = n * factor[0] // gcd(n, factor[0])
    return lcm
def test_largest_divisor():
    assert largest_divisor(15) == 5
```