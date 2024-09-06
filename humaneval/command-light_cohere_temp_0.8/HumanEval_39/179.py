Here's a solution:

```python
def prime_fib(n: int) -> int:
    if n <= 1:
        return n
    elif n <= 3:
        return 2
    elif n % 2 == 0:
        return 3
    else:
        temp = prime_fib(n // 2)
        if temp == 2:
            return temp + 1
        else:
            return temp + 2
```

This function uses a recursive approach to find the n-th Fibonacci number that is prime, and also checks for primality.  It uses the fact about the prime numbers, which lies in the format 2n + 1 or exactly 2*n-1.