
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
    res = []
    mid = (n + m) / 2
    if mid < m:
        return -1

    for i in range(n, mid):
        res.append(bin(i))

    if mid == m:
        return bin(mid)

    if mid < m:
        for i in range(m - mid):
            res.append(bin(mid + i + 1))

    res = sorted(res, key=len)
    for i in range(len(res)):
        res[i] = res[i].split('b')[1]

    return "".join(res)