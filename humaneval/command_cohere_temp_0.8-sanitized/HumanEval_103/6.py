def rounded_avg(n, m):
    total = (n + m) // 2
    count = 1
    while count < m:
        total += n
        count += 1
    avg = total / count
    return bin(round(avg))[2:]