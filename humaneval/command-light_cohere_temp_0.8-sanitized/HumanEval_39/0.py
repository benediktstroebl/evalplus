def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 3
    else:
        temp = prime_fib(n // 2)
        if temp == 2 or temp == 3:
            return temp
        else:
            return 2 + (prime_fib(n - temp) - 1)