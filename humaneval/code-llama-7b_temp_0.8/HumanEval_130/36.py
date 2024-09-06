
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
    # It's important to note that tri(1) is 3 (not 1), so we add that to our result.
    result = [1, 3]
    # Then we start the iteration, starting from 2 because we already have the first two
    # numbers. We also have to have the previous two numbers.
    prev_1 = 1
    prev_2 = 3
    # Finally, we iterate until n is 0, which is when we're done.
    for i in range(2, n + 1):
        # We keep track of our current value as sum, and add it to our result
        result.append(sum([prev_1, prev_2, prev_1 + prev_2]))
        # Then, we swap prev_1 and prev_2 so that they're the last two numbers.
        prev_1, prev_2 = prev_2, result[-1]
    return result
