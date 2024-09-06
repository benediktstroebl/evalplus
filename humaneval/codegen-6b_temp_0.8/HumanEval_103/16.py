
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
    n_binary = bin(n)[2:]
    m_binary = bin(m)[2:]
    n_length = len(n_binary)
    m_length = len(m_binary)
    total = 0
    for i in range(n_length):
        total += int(n_binary[-(i+1)]) * int(m_binary[-(i+1)])
    return int(str(bin(total)[2:])[::-1], 2)


