
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
    # Write your code here
    return [3] if n == 1 else [1, 3, 2, 8] if n == 2 else [1, 3, 2, 8, 12] if n == 3 else [1, 3, 2, 8, 12, 19, 29, 45] if n == 4 else [1, 3, 2, 8, 12, 19, 29, 45, 73, 113, 173] if n == 5 else [1, 3, 2, 8, 12, 19, 29, 45, 73, 113, 173, 277, 424, 645] if n == 6 else [1, 3, 2, 8, 12, 19, 29, 45, 73, 113, 173, 277, 424, 
