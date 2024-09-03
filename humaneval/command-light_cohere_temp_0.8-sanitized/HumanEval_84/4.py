def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary"""
    # convert integer to binary
    sum_bin = 0
    while N > 0:
        sum_bin += int(N % 2)
        N = N // 2
    # convert sum back to string
    return "".join(str(sum_bin))