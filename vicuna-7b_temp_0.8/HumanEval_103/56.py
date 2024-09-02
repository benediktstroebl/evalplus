
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
    n_sum = n
    m_sum = m
    sum = 0
    for i in range(n, m+1):
        sum += i
        n_digit = sum // (n-1)
        m_digit = sum // (m-1)
        if n_digit >= 10 and m_digit >= 10:
            n_digit = n_digit // 10
            m_digit = m_digit // 10
            n_sum = n_sum // 10
            m_sum = m_sum // 10
            binary_n = str(n_sum)
            binary_m = str(m_sum)
            while binary_n.startswith("0") and binary_m.startswith("0"):
                binary_n = binary_n[1:]
                binary_m = binary_m[1:]
            binary_n = binary_n.rjust(10, '0')
            binary_m = binary_m.rjust(10, '0')
            return binary_n + binary_m
        else:
            return str(n_digit).rjust(10, '0') + str(m_digit).rjust(10, '0')
    return -1