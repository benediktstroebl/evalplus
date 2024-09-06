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
    prev_fib, curr_fib = 1, 2
    for _ in range(n - 1): 
        prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
    # checks for both prime and fibonacci criteria are done separately
    # this loop is needed only for the prime criterion
    for _ in range(n):
        if not is_prime(curr_fib):
            curr_fib += 1
            continue
        return curr_fib