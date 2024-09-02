

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
    # source of the challenge
    # https://www.glassdoor.com/Interview/Element-at-location-14601276-or-Element-at-location-14601276-or-Element-at-location-14601276-QTN_11144132.htm
    # https://www.glassdoor.com/Interview/Solve-Element-at-location-14601276-or-Element-at-location-14601276-QTN_11144133.htm

    # we create a table of all the previous results
    # and then we start filling them in
    # 0, 0, 2, 0, 8, 0, 26, 0, 88, 0, 298, 0, 944, 0, 3868
    table = [0] * (n + 1)
    table[0] = 0
    table[1] = 0
    table[2] = 2
    table[3] = 0
    table[4] = 8
    table[5] = 0
    table[6] = 26
    table[7] = 0
    table[8] = 88
    table[9] = 0
    table[10] = 298
    table[11] = 0
    table[12] = 944
    table[13] = 0
    table[14] = 3868
    for index in range(n + 1)[4:]:
        table[index] = table[index - 1] + table[index - 2] + table[index - 3] + table[index - 4]
    return table[-1]

