
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
    if not (isinstance(n, int) and isinstance(m, int) and n >= 0 and m >= 0):
        raise ValueError("Inputs must be positive integers!")

    if n > m:
        return -1

    n_b, m_b = bin(n)[2:], bin(m)[2:]
    n_len, m_len = len(n_b), len(m_b)

    avg = 0
    for i in range(n_len):
        if i >= m_len:
            break

        avg += int(n_b[i])
        avg += int(m_b[i])

    return bin(avg)[2:]
