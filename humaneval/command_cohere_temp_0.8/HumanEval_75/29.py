```python
def is_multiply_prime(a):
    # Check if a is less than 100
    if a < 100:
        # Count the unique divisors of the number a
        div = set(int(d) for d in factorize(a) if d > 1)
        # Check if the number is the multiplication of exactly 3 primes
        return len(div) == 3
    else:
        return False

def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(int(n))
    return factors
``` 

This Python code defines a function, `is_multiply_prime`, which assesses whether a given number `a` is the product of three prime integers. To accomplish this, the code utilizes a `factorize` helper function to extract the distinct divisors of `a`, and then checks if their count equals 3, indicating the presence of exactly three distinct prime factors. This condition is met for `a = 30`, resulting in the function returning `True`, while cases like `a = 4` or `a = 6` yield `False`, as they have fewer than three prime factors.