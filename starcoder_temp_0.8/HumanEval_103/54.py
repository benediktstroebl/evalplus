
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
    n = bin(n)[2:]
    m = bin(m)[2:]
    if len(n) > len(m):
        return -1
    if len(n) < len(m):
        n = (m[:len(n) - len(m)]) + n
    n = int(n)
    m = int(m)
    avg = (n + m) / 2
    avg = int(avg)
    avg = bin(avg)[2:]
    return "0b" + avg
