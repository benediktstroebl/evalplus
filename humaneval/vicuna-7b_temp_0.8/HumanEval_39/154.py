

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
    def get_fib(n):
        # Checking if n is prime
        if n > 2:
            if n % 2 == 0:
                return n / 2
            else:
                return n + (n - 2) // 2

        # If n is not prime then return the previous number
        return get_fib(n - 1)

    if n < 2:
        return 1

    # Get the previous number
    a, b = 0, 1
    prev = a

    # Iterating from 2 to n
    for i in range(2, n + 1):
        # Checking if the current number is prime
        if get_fib(i) == i:
            # If it's prime, we append the current number and the previous number to the list
            fib_list.append(i)
            fib_list.append(prev)
            prev = i
        else:
            fib_list.append(i)

    # Returning the n-th number in the list
    return fib_list[n - 1]
