```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if all(int(d) <= x for x in factors(n, d))), n+1

def factors(n: int, d: int) -> bool:
    return (d==1 or any(int(k) > d and n%k == 0 for k in range(1, d))) and (n!=1)
```
This code defines a function `largest_divisor` that finds the largest divisor of a given number `n` by iterating through divisors from 1 to `n`, and checking if they are all less than all factors of `n`. The function also utilizes a helper function `factors` to check if a given divisor `d` is a factor of `n`.