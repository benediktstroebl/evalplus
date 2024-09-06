def rounded_avg(n, m):
    total = (m + n) // 2
    count = 1
    idx = n
    while idx <= m:
        total += idx
        count += 1
        idx += 1
    if count % 2 == 0:
        return '0b' + str(total).zfill(len(str(m + n)))
    else:
        return '0b' + str(total + 1).zfill(len(str(m + n)))