

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
    # Create a list of n-1 and n-2 values
    a = [fib4(n-1), fib4(n-2)]

    # Combine the two values to form the first part of the n-th value
    a_sum = a[0] + a[1]

    # Combine the first part of the n-th value with the next n-3 values to form the second part of the n-th value
    b_sum = fib4(n-3) + fib4(n-4)

    # Combine the first and second parts of the n-th value to form the final result
    b_sum = b_sum + (a_sum % 2)

    return b_sum
