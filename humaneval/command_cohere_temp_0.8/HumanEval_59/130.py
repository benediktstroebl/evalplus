```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Quick cheat-sheet for prime factors:
    # 1. Starting from 2, divide n by 2 until it becomes odd
    # 2. Starting from the oddest remaining factor, divide n by the next odd number until you reach a factor less than yourself
    # 3. For any remaining factors, divide n by them self repeatedly until it is 1
    if n % 2:
        return 2
    while n % 2 == 0:
        n //= 2
    a = 3
    b = (len(str(n)) - 1) // 2
    for _ in range(b + 1):
        if n % a:
            return a
        while n % a == 0:
            n //= a
            if a == b:
                break
            a += 2
    for c in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        while n % c == 0:
            n //= c
    if n > 1:
        return n
```