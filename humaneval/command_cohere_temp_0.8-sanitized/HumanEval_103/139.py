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
    elif count == m:
        return bin(round(total))[2:].zfill(64)
    else:
        avg = total + (m - count)
        return bin(round(avg))[2:].zfill(64)