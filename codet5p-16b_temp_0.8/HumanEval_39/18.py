

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

    fib_numbers = [1, 1, 2]
    count = 3
    while count < n:
        fib_numbers.append(fib_numbers[count-1] + fib_numbers[count-2])
        count += 1
    for number in fib_numbers:
        if number > 1:
            for divider in range(2, number):
                if number % divider == 0:
                    break
            else:
                return number

