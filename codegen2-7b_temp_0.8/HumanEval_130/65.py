
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
    if n <= 2:
        return [1, 1, 2, 4]
    previous_tribonacci = 1
    current_tribonacci = 1
    next_tribonacci = 1
    tribonacci_sequence = [current_tribonacci]
    for _ in range(n - 1):
        previous_tribonacci, current_tribonacci, next_tribonacci = current_tribonacci, next_tribonacci, previous_tribonacci + current_tribonacci
        tribonacci_sequence.append(next_tribonacci)
    return tribonacci_
