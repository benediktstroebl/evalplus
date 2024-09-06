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
    rounded_avg = total
    binary_representation = '{0:b}'.format(rounded_avg)
    return binary_representation