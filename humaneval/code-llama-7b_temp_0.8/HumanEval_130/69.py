
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
    def _tri(n):
        if n == 1:
            yield 1
        elif n == 2:
            yield 1
            yield 3
        elif n == 3:
            yield 1
            yield 3
            yield 2
        else:
            pre1 = 1
            pre2 = 3
            pre3 = 2
            yield pre1
            yield pre2
            yield pre3
            while n > 3:
                pre1, pre2, pre3 = pre2, pre3, pre1 + pre2 + pre3
                yield pre1
                n -= 1

    return list(_tri(n))

