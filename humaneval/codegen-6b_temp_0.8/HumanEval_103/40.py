
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
    binary_n = to_binary(n)
    binary_m = to_binary(m)
    total = 0
    for b_n, b_m in zip(binary_n, binary_m):
        if b_n == b_m:
            total += b_n
        elif b_n > b_m:
            return -1
    return to_integer(total)


from math import ceil