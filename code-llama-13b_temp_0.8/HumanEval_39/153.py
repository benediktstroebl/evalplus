

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
    # we'll use these to save some calculations
    memo_is_prime = [True] * (10 ** 6)
    memo_is_prime[0] = False  # 0 isn't prime
    memo_is_prime[1] = False  # 1 isn't prime
    memo_is_fib = [False] * (10 ** 6)

    # we'll get a list of prime numbers up to 10**6
    # thanks to this: https://stackoverflow.com/a/58127818
    prime_numbers = [2, 3, 5]
    for number in range(6, 10 ** 6, 10):
        prime_numbers.extend(
            [
                prime_number
                for prime_number in range(number, number + 10, 2)
                if is_prime(prime_number, memo_is_prime)
            ]
        )

    # we need to check only even Fibonacci numbers
    # because if Fib(x) is even then Fib(x+1) is odd and vice versa
    for number in prime_numbers:
        if number > 10 ** 6:
            break
        # we know that 3 is not a Fibonacci number
        if number == 3:
            continue
        if is_fib(number, memo_is_fib):
            return number

