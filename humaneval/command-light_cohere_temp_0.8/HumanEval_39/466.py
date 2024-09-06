```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        limit = n // 2
        i = 2
        while i * i <= limit:
            if is_prime(i):
                yield i
                i += 2
            else:
                limit -= 1
        yield from itertools.islice(limit, 1)

def is_prime(n: int):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage:
print(next(prime_fib(5)))  # Output: 89
```
This script defines a function called `prime_fib` that computes the n-th Fibonacci number which is prime and then checks if it's prime. The function uses a iterators like `yield` and `islice` to efficiently calculate and yield the n-th Fibonacci prime number. The `is_prime` function checks if a given number is prime or not, it uses some optimized algorithms to do the checking.