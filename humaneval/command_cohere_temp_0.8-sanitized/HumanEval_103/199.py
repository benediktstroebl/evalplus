def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    rounded = avg % 1
    return '0b' + bin(int(rounded * 2))[2:][:1]