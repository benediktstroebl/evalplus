

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

    if n == 1:
        return 2
    else:
        fib_num = [1, 1]
        current_num = 2
        while len(fib_num) < n:
            current_num = fib_num[-1] + fib_num[-2]
            if current_num > 4000000:
                raise ValueError('Invalid Input.  Please check your code!')
            elif current_num > 0:
                for num in range(2, int(current_num ** 0.5) + 1):
                    if current_num % num == 0:
                        break
                else:
                    fib_num.append(current_num)
            else:
                fib_num.append(current_num)
        for num in range(2, len(fib_num)):
            if len([x for x in range(2, fib_num[num]) if fib_num[num] % x == 0]) == 0:
                return fib_num[num]

