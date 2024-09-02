
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # 遍歷整貪數，尋找 n-1 的整數
    n_ones = 0
    while n != 0:
        n = n // 10
        n_ones += 1
    # 判斷預計的答案是否正確
    ans = 1 + n_ones // 2
    return ans
