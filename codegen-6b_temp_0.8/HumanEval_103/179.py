
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
    # rounded_avg = (n + m) / 2
    # # if rounded_avg.bit_length() > 31:
    # #     return -1
    # # elif rounded_avg.bit_length() <= 31:
    # #     return f'0b{rounded_avg:b}'
    if m == n:
        return f'0b{n:b}'

    # elif m > n:
    #     return -1
    # else:
    #     if (n + m) % 2 == 0:
    #         return rounded_avg
    #     else:
    #         return f'0b{rounded_avg:b}'
    return -1
