def rounded_avg(n, m):
    if n > m:
        return -1
    num = (n + m) // 2
    bin_str = bin(round(num))[2:]
    return bin_str if len(bin_str) < 10 else bin_str[:1]