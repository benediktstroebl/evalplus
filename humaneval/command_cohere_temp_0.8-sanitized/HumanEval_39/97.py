def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    if n < 1:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        x, y = 0, 1
        for i in range(n - 1):
            x, y = y, x + y
        return prime_check(x)
def prime_check(n):
    if is_prime(n):
        return n
    return None