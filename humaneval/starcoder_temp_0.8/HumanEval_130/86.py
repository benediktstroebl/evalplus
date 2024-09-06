
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
    assert isinstance(n, int), 'n must be an integer'
    assert n >= 0, 'n must be non-negative'
    first = 3
    second = 1
    third = 2
    lst = []
    for i in range(n+1):
        if i == 0:
            continue
        elif i % 3 == 0:
            first = second + third
            second = third + first
            third = first + second
            lst.append(first)
        elif i % 3 == 1:
            second = first + third
            third = second + first
            first = third + second
            lst.append(second)
        elif i % 3 == 2:
            third = second + first
            first = third + second
            second = first + third
            lst.append(third)
    return lst
