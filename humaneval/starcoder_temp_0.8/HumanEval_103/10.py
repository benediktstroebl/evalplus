
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

    # Taking abs value of (n-m) because the difference
    # between the numbers must be positive
    # we can't have negative difference between n and m
    abs_n_m = abs(n - m)
    # if difference between n and m is even, the answer is average of n and m
    # if difference between n and m is odd, the answer is average of n+1 and m
    if abs_n_m % 2 == 0:
        return bin(int(n + m / 2))
    else:
        return bin(int(n + m / 2 + 1))
