
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
    # list to store the tribonacci sequence
    seq = []
    
    # check if n is even or odd
    if n % 2 == 0:
        # if n is even, add 1 to the previous number
        seq.append(n + 1)
        # add 3 to the seq
        seq.append(3)
        seq.append(1)
    else:
        # if n is odd, calculate the tribonacci number
        seq.append(tri(n - 2) + tri(n - 1) + tri(n + 1))
    
    # return the seq
    return seq
