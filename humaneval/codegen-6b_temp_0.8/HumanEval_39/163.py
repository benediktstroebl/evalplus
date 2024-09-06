

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
    number = fibonacci_numbers(n)
    prime_numbers = [2, 3, 5]
    if n < 2:
        return number
    else:
        while True:
            for i in range(2, number):
                if number % i == 0:
                    number = number // i
                    break
            if number > 1:
                prime_numbers.append(number)
            else:
                break
    return prime_numbers[n - 1]

