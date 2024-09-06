```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    # Compute all divisors of a and b
    divisors_a = [i for i in range(1, int(a**0.1) + 1)]
    divisors_b = [i for i in range(1, int(b**0.1) + 1)]
    
    for i, div in zip(divisors_a, divisors_b):
        if a % div != 0 and b % div != 0:
            return div

    # If no shared divisor, both numbers are prime
    return 2 ** (min(math.log(a), max(math.log(b), time(a)))
```