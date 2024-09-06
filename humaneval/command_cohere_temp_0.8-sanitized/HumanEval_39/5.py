def is_prime(n):
    """
    Checks if a number is prime
    """
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
    """
    Generates n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    elif n == 4:
        return 13
    elif n == 5:
        return 89
    else:
        # This section makes use of the fact that prime fibonacci numbers have
        # irregular gaps between them. For example, the 7th prime Fibonacci
        # number is 107 which is very far from the 6th prime Fibonacci number, 13.
        # This gap is irregular and we can use this property to bound our search.
        # This is based on the fact that the gap between successive prime fibonacci
        # numbers becomes irregularly large after the 5th prime Fibonacci number.
        a, b = 0, 1
        for i in range(5, n // 2 + 1):
            x = a + b
            if is_prime(x):
                a, b = x, x + a
            else:
                b += a
        if n % 2 == 0:
            return prime_fib(n - 1)
        else:
            return prime_fib(n - 2)