def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        a, b = 2, 3
        for _ in range(n - 1):
            if is_prime(a):
                b = a
            a += 1
        return b
def is_prime(num: int):
    if num <= 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True