
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
    
    n_s = str(bin(n)[2:])
    m_s = str(bin(m)[2:])
    avg_s = str(bin(int((n + m) / 2))[2:])
    for i in range(len(n_s), len(m_s)):
        n_s = "0" + n_s
    for i in range(len(m_s), len(avg_s)):
        m_s = "0" + m_s
    
    return int(n_s + avg_s, 2)

