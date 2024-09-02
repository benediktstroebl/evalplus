
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
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    if n == 3:
        return [1, 1, 1]
    if n > 3:
        result = [1, 1, 1]
        new_arr = [1, 1, 1]
        old_arr = result[1:]
        for i in range(3, n+1):
            new_arr.append(sum(result[-3:]))
            new_arr[0] = result[0]
            new_arr.append(sum(result[-3:]))
            old_arr.insert(0, result[0])
            old_arr.append(result[1])
            result = list(old_arr)
        return result
