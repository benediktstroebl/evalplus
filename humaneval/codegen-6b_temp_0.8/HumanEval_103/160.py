
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
    mid = (n + m) // 2
    if m - n == 1:
        return "0b1"
    elif sum(int(_) for _ in bin(mid)[2:]) > sum(int(_) for _ in bin(m)[2:]):
        return -1
    else:
        return "0b{0:b}".format(mid)

