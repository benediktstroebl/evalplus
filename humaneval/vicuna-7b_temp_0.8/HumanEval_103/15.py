
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
    average = (n + m) / 2
    n_bin = to_binary(n)
    m_bin = to_binary(m)
    bin = n_bin + m_bin + "0"*(2-len(n_bin)-len(m_bin))
    return bin.rjust(len(average), "0")[2:-2]