
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
    # This is a variation of the recursive approach, where you 
    # build the sequence in memory by appending the previous 
    # values to a list, and then return the entire list at the end.
    # Here we use a list to store the current values, and 
    # the append method to add the next value to the list
    current = [0]
    next_value = [0]
    result = []
    for value in range(n + 1):
        result.append(current[-1])
        current.append(next_value[-1])
        next_value = current
        next_value.append(value)
    result.extend(current)
    return result