

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    if n < 2:
        return 1

    if n < 10:
        return prime_fib(n)

    if n % 2 == 0:
        return 3

    if n % 3 == 0:
        return 5

    while True:
        if n % 2 == 1:
            return n
        n += 2

prime_fib_check = []

for i in range(1, 11):
    if prime_fib(i) == i:
        prime_fib_check.append(i)

for i in prime_fib_check:
    print(i)

if prime_fib(n) % n != 0:
    print("Error")
else:
    print("Correct")