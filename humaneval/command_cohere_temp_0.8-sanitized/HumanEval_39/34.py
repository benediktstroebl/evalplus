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
    fib_nums = [0, 1]
    for _ in range(n - 1):
        next_num = fib_nums[-1] + fib_nums[-2]
        fib_nums.append(next_num)
    for num in fib_nums:
        if is_prime(num):
            return num