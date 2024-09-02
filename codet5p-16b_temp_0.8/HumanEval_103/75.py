
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
    n_bin = str(bin(n))[2:]
    m_bin = str(bin(m))[2:]
    len_n_bin = len(n_bin)
    len_m_bin = len(m_bin)
    if len_n_bin < len_m_bin:
        n_bin = "0" * (len_m_bin - len_n_bin) + n_bin
    elif len_n_bin > len_m_bin:
        m_bin = "0" * (len_n_bin - len_m_bin) + m_bin
    rounded_avg = int(round((n + m)/2))
    avg_bin = str(bin(rounded_avg))[2:]
    len_avg_bin = len(avg_bin)
    if len_avg_bin < len_m_bin:
        avg_bin = "0" * (len_m_bin - len_avg_bin) + avg_bin
    el
