
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
    if n >= m:
        return -1
    n_bin = format(n, "b")
    m_bin = format(m, "b")
    i = 0
    sum_bin = ""
    while i < len(n_bin):
        sum_bin += n_bin[i]
        i += 1
    i = 0
    while i < len(m_bin):
        sum_bin += m_bin[i]
        i += 1
    print(sum_bin)
    return sum_
