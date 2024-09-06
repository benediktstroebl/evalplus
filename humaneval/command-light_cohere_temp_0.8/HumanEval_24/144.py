```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n+1) if any(x % y for y in range(1, n+1)) == 0))
``` 
This Python function uses the generator expression with the any function to check all divisors of numbers ranging from 1 to the given number n, and returns the largest number among them that does not produce any division by any of these numbers.  This largest_divisor(15) would return 5, which is the largest divisor of 15.