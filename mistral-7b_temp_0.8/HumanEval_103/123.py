
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

    # Write your code here
    if n > m:
        return -1

    # convert n and m to binary
    n_bin = bin(n)
    m_bin = bin(m)

    # convert n_bin and m_bin to list of 0 and 1
    n_list = list(n_bin[2:])
    m_list = list(m_bin[2:])

    # if n and m are both even numbers
    if n % 2 == 0 and m % 2 == 0:
        # loop through n_list and m_list
        for i in range(len(n_list)):
            # if the n_list[i] is 1, add 1 to m_list[i]
            if n_list[i] == '1':
                m_list[i] = '1'
            # if the m_list[i] is 1, add 1 to n_list[i]
            if m_list[i] == '1':
                n_list[i] = '1
