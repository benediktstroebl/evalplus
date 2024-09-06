
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
    else:
        n = n + 1
        m = m - 1
        n_sum = 0
        m_sum = 0
        for i in range(n, m + 1):
            n_sum += i
        for j in range(n, m + 1):
            m_sum += j
        n_sum = int(n_sum)
        m_sum = int(m_sum)
        print(bin(n_sum))
        print(bin(m_sum))
        print(format(float((n_sum + m_sum) / (n + m)), '.2f'))


rounded_avg(2, 3)
rounded_avg(10, 10)
rounded_avg(1, 5)
rounded_avg(5, 1)
rounded_avg(20, 33)