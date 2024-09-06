

def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n < 0:
        raise ValueError('n must be >= 0')
    # These are the first three numbers in the sequence
    if n <= 2:
        return 0
    # Create a table with the first 3 numbers
    table = [0, 0, 1]
    # For each number after the third, calculate the next fibfib and put it in the table
    for i in range(3, n + 1):
        table.append(table[i - 1] + table[i - 2] + table[i - 3])
    return table[n]

