```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        # Check if n is a perfect square
        sqrt_n = int(math.sqrt(n))
        if sqrt_n * sqrt_n <= n:
            return n
        else:
            # Check divisors of n less than sqrt_n
            for i in range(5, int(sqrt_n / 2) + 1):
                if n % i == 0:
                    return i
                    break
            return n
```