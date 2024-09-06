def rounded_avg(n, m):
    total = (m + n) // 2
    count = 1
    if n > m:
        return -1
    while m - n > 1:
        if m >= n:
            digits = str(m)
        else:
            digits = str(n)
        if int(digits[-1]) == 1:
            count += 1
        total += count
        if m > n:
            m //= 2
        else:
            n //= 2
    if m - n == 1:
        if m >= n:
            digits = str(m)
        else:
            digits = str(n)
        if int(digits[-1]) == 1:
            count += 1
        total += count
    rounded_total = int(total)
    return f"0b{bin(rounded_total)[2:]}"