

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
    index = 2
    current_fib = 0
    previous_fib = 1
    prime_list = [2]

    while True:
        # Swap current and previous
        current_fib, previous_fib = previous_fib, current_fib + previous_fib

        if current_fib % 2 != 0:
            # If the number is odd, check if it's prime
            for prime in prime_list:
                if current_fib % prime == 0:
                    break
                elif prime >= current_fib ** 0.5:
                    prime_list.append(current_fib)
                    if index == n:
                        return current_fib
                    break

            if index == n:
                return current_fib
            else:
                index += 1

