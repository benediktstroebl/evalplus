
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
    # YOUR CODE HERE
    s = ''
    ans = 0
    n = int(n)
    m = int(m)
    if n > m:
        return -1
    if n < 0 or m < 0:
        return -1
    if n == m:
        return str(bin(n))
    for i in range(n, m + 1):
        ans += i
    if ans == 0:
        return '0b'
    ans = ans / (m - n)
    ans = round(ans)
    ans = bin(ans)
    ans = ans[2:]
    ans = '0b' + ans
    return ans
