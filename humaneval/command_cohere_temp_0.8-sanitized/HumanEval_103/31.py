def rounded_avg(n, m):
    total = (m + n) // 2
    count = 1
    prev = n
    while count <= m:
        if prev + 1 == m:
            break
        if prev + 2 <= m:
            count += 1
        else:
            count = m - prev
        prev = prev + 1
    if n >= m:
        return -1
    binary_string = bin(round(total))[2:]
    return binary_string if binary_string[0] == '1' else binary_string[1:]