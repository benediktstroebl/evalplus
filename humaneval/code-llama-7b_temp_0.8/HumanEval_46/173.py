

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

    # Creating an array to hold the value of the series.
    array = [0] * (n+1)

    # Setting the first two elements of the array
    array[0] = 0
    array[1] = 0
    array[2] = 2

    # Initialising i, used to iterate through the array.
    i = 3

    # Iterating through the array until i > n.
    while i <= n:
        # Setting the current element of the array to be equal to the sum of the previous four elements.
        array[i] = array[i-1] + array[i-2] + array[i-3] + array[i-4]
        # Incrementing i.
        i += 1

    # Returning the n-th element of the series.
    return array[n]

