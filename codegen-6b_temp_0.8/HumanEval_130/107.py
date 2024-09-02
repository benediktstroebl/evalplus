
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
    nums = [-1] * (n + 1)
    nums[1] = 1
    if n < 1:
        return nums
    if n == 1:
        return nums[1:]

    nums[2] = 1
    if n == 2:
        return nums[1:]
    
    nums[3] = 3
    if n == 3:
        return nums[1:]
    
    for i in range(4, n + 1):
        nums[i] = (nums[i-2] + nums[i-1] + nums[i-3]) % 10

    return nums[1:]
