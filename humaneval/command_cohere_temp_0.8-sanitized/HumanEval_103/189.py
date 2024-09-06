def rounded_avg(n, m):
    diff = m - n
    avg = (n + m) // 2
    rounded_avg = (-1 if diff < 0 else bin(avg)[2:].rjust(32, '0'))
    return rounded_avg