def rounded_avg(n, m):
    bin_str = [-1 if i == 0 else '0' for i in range(m - n + 1)]
    if n > m:
        return -1
    for i in range(n, m + 1):
        bin_str[i - n] = str(bin(i - n + 1)[2:])
    return '0b' + ''.join(bin_str)