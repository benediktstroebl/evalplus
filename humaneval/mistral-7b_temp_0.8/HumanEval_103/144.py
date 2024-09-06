
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
    # convert numbers to binary and add them
    # check if n is bigger than m
    # if n is bigger, convert to binary and return -1
    # else return binary
    if n > m:
        return bin(-1)
    n_bin = bin(n)[2:]
    m_bin = bin(m)[2:]
    total = int(n_bin) + int(m_bin)
    avg = total / 2
    return bin(avg)
