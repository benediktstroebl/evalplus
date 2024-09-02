

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
    def fib(n: int):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return fib(n-1) + fib(n-2)

    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    i = 1
    while True:
        if fib(i) % 2 != 0 and is_prime(fib(i)):
            if n == 1:
                return fib(1)
            if n == 2:
                return fib(2)
            if n == 3:
                return fib(3)
            if n == 4:
                return fib(4)
            if n == 5:
                return fib(5)
            if n == 6:
                return fib(6)
            if n == 7:
                return fib(7)
            if n == 8:
                return fib(8)
            if n == 9:
                return fib(9)
            if n == 10:
                return fib(10)
            if n == 11:
                return fib(11)
            if n == 12:
                return fib(12)
            if n == 13:
                return fib(13)
            if n == 14:
                return fib(14)
            if n == 15:
                return fib(15)
            if n == 16:
                return fib(16)
            if n == 17:
                return fib(17)
            if n == 18:
                return fib(18)
            if n == 19:
                return fib(19)
            if n == 20:
                return fib(20)
            if n == 21:
                return fib(21)
            if n == 22:
                return fib(22)
            if n == 23:
                return fib(23)
            if n == 24:
               
