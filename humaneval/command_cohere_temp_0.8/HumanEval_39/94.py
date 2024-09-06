```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_fib(n):
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        prime_idx = 0
        fib_idx = 0
        curr_prime = 5
        while prime_idx < n:
            if is_prime(curr_prime):
                if prime_idx == n - 1:
                    return curr_prime
                prime_idx += 1
            curr_prime = fib_sequence[fib_idx]
            fib_idx = (fib_idx + 1) % 2
        return None

fib_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229]
```