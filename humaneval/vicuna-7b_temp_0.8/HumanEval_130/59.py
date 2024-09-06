
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
    # initialize variables
    a = 0
    b = 1
    c = 1
    d = 0
    n = n + 1

    # loop through the sequence
    for i in range(n):
        # handle even cases
        if i % 2 == 0:
            # add tri(i - 1) + tri(i - 2) + tri(i + 1)
            d = (c * (i - 2)) + (b * (i - 1)) + (a * (i + 1))
        # handle odd cases
        else:
            # loop through the even cases and add them up
            d = tri(i - 1) + tri(i - 2) + tri(i + 1)

        # append the value to the list
        yield d

        # update variables for the next iteration
        a, b, c = b, c, d

    # append the final value to the list
    yield d
