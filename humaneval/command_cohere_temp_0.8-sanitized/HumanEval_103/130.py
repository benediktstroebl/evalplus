def rounded_avg(n, m):
    if n > m:
        return -1
    num = (n + m) // 2
    rounded_num = round(num)
    return bin(rounded_num)[2:]