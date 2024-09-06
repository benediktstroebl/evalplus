
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
    if n>m:
        return -1
    elif n==m:
        return '0b'+str(n)
    else:
        mean=round((m+n)/2)
        if mean==n:
            return '0b'+str(mean)
        else:
            return bin(mean)
    
    # # another solution
    # if n > m:
    #     return -1
    
    # def binary_rep(n):
    #     r = ''
    #     while n:
    #         r = str(n % 2) + r
    #         n //= 2
    #     return r
    
    # mid = (m + n) // 2
    # return binary_rep(mid)
