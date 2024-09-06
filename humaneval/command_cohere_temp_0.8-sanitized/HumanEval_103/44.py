def rounded_avg(n, m):
    total = (m + n) // 2
    count = m - n + 1
    answer = bin(round(total / count))[2:]
    if n > m:
        return -1
    else:
        return answer