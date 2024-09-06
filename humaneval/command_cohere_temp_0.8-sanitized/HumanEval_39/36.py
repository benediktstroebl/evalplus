def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    if n < 1:
        return None
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x + y
    if is_prime(x):
        return x
    return None