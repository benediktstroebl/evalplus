
def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    # initialize variables to store the sequence
    n1 = n
    n2 = n + 2
    n3 = n + 1
    sequence = []
    while True:
        if n1 % 2 == 0:
            sequence.append(n1)
            n1 = n2
        elif n1 == n2:
            n3 = n1
            sequence.append(n1)
            n1 = n2
        else:
            n3 += n2
            n2 += n1
            n1 = n3
            sequence.append(n1)
    return sequence
