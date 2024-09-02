

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
    # Create a list to store the sum of the fibonacci numbers
    fib_list = []

    # Calculate and store the sum of the first 16 fibonacci numbers
    for i in range(16):
        fib_list.append(fib3(i))

    # Calculate and return the sum of the fibonacci numbers up to n
    return fib_list[-1] + fib_list[-2] + fib_list[-3] + fib_list[-4]
