

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
    # create an empty list
    prime_fib_numbers = []
    # create an empty list of odd Fibonacci numbers
    fib_odd = []
    # start the Fibonacci sequence with 1 and 1
    fib = 1
    # start the Fibonacci sequence with 0 and 1
    prev = 0
    # iterate through the Fibonacci sequence
    while fib < 2**64:
        fib_odd.append(fib)
        fib, prev = fib + prev, fib
    # iterate through the Fibonacci sequence and find the primes
    for number in fib_odd:
        if number > 2:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                prime_fib_numbers.append(number)
    # return the n-th prime Fibonacci number
    return prime_fib_numbers[n - 1]

