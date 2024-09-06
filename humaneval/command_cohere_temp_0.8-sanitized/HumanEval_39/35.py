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
    num = 0
    prev_num = 1
    while num <= n:
        num, prev_num = prev_num, num + prev_num
        if is_prime(num):
            return num
    return None