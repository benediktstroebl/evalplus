
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
    if m < n:
        return -1
    delta = m - n
    k = 1
    total = 0
    while delta > 0:
        total += k * (2 ** delta)
        delta -= 1
        k += 1
    if k > 1:
        return total.to_bytes(k, 'little').lstrip(b'\x00')
    elif k == 1:
        return '\x01'
    else:
        return -1

