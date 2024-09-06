def rounded_avg(n, m):
    total = (m + n) // 2
    count = 1
    prev = n
    while count < m:
        if prev + 1 < m:
            prev += 1
            count += 1
        else:
            break
    if n > m:
        return -1
    avg = total
    if prev == m:
        return bin(avg)[2:].zfill(64)
    else:
        return bin(avg + 1)[2:].zfill(64)