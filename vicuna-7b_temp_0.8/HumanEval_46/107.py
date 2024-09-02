

def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """

    # Find the last two digits in the n-th position
    last_two_digits = n // 2
    remainder = n % 2

    # Compute the sums of the fibonacci numbers
    sum_1 = fib4(last_two_digits) + fib4(last_two_digits-1)
    sum_2 = fib4(last_two_digits-2) + fib4(last_two_digits-3)

    # Combine the sums and return the result
    result = sum_1 + sum_2 + remainder
    return result