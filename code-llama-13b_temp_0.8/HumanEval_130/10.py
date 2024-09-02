
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
    #initialize a list
    tri_sequence = [0] * (n+1)
    
    #use indices as the n-1, n, n+1
    for i in range(n+1):
        #base case
        if i == 0:
            tri_sequence[i] = 0
        #next two if statements are defining the base case tri(1) = 3
        elif i == 1:
            tri_sequence[i] = 3
        #if odd number then tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1)
        elif i % 2 != 0:
            tri_sequence[i] = tri_sequence[i-1] + tri_sequence[i-2] + tri_sequence[i+1]
        #if even number then tri(n) = 1 + n / 2, 
        else:
            tri_sequence[i] = 1 + i/2
    return tri_sequence
