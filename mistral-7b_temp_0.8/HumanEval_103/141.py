
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
    n_list = [n, n+1, n+2, n+3, n+4, n+5, n+6]
    m_list = [m, m+1, m+2, m+3, m+4, m+5, m+6]
    avg = sum(n_list) / len(n_list)
    avg = sum(m_list) / len(m_list)
    avg = round(avg)
    avg = int(avg)
    avg = bin(avg)
    avg = avg[2:]
    return avg
