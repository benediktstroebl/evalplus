
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
    # The first n numbers of the Tribonacci sequence are 
    # tri(0), tri(1), tri(2), ... , tri(n-1)
    # The first n + 1 numbers of the Tribonacci sequence are 
    # tri(0), tri(1), tri(2), ... , tri(n)
    #
    # We will use a recursive approach to compute the first n + 1 numbers of the 
    # Tribonacci sequence.
    #
    # Here's the implementation:
    #
    #
    # To compute the first n numbers of the Tribonacci sequence, 
    # we need to compute the first n + 1 numbers of the Tribonacci 
    # sequence, and discard the last number. 
    #
    # To compute the first n + 1 numbers of the Tribonacci sequence, 
    # we need to compute the first n numbers of the Tribonacci 
    # sequence, and add the first number to the first n + 1 numbers.
    #
    # To compute the first n numbers of the Tribonacci sequence, 
    # we need to compute the first n - 1 numbers of the Tribonacci 
    # sequence, and add the last two numbers to the first n numbers.
    #
    # It's a bit tricky to implement all of this, so we will use a 
    # helper function tri_helper that does the hard work for us.
    #
    #
    # The helper function tri_helper takes a non-negative integer 
    # n and returns a list of the first n + 1 numbers of the Tribonacci 
    # sequence.
    #
    # Here's the implementation of tri_helper:
    def tri_helper(n):
        if n <= 0:
            return []
        if n % 2 == 0:
            return [tri_helper(n // 2)]
        return tri_helper(n - 1) + [tri_helper(n - 2), tri_helper(n - 1) + tri_helper(n + 1)]
    return tri_helper(n)
