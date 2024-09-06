

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
    # Creating an empty list to store the fibonacci numbers
    fibs = [0] * n

    # Generating the first 4 fibonacci numbers
    fibs.append(1)
    fibs.append(1)
    fibs.append(1)
    fibs.append(1)

    # Using a loop to compute the n-th fibonacci number
    for i in range(1, n):
        fibs[i] = fibs[i-1] + fibs[i-2] + fibs[i-3] + fibs[i-4]

    return fibs[n-1]