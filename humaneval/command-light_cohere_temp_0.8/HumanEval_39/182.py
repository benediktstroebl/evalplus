```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    else:
        limit = n
        prev = 2
        while True:
            if is_prime(prev) and prev <= limit:
                limit -= 1
                yield prev
                prev += 2
            else:
                break
        yield limit

def is_prime(n: int):
    # using the sieve of Eratosthen
    divs = range(2, int(n**0.2) + 1)
    for i in divs:
        if n % i == 0:
            return False
    return True

# Example usage
for n in prime_fib(10):
    print(n, end=' ')
```