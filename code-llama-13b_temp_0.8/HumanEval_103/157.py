
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    if n > m:
        return -1
    # prev number 
    prev = n - 1
    # next number
    next = n + 1
    # get the avg of n and m
    average = (m + n) / 2
    # get the rounding of the avg
    rounding = round(average)
    # check if prev number is even and next number is odd
    if (prev % 2 == 0 and next % 2 == 1):
        if (average == rounding):
            return bin(rounding)
        else:
            return bin(prev)
    # check if prev number is odd and next number is even
    if (prev % 2 == 1 and next % 2 == 0):
        if (average == rounding):
            return bin(rounding)
        else:
            return bin(next)

