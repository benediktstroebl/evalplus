def rounded_avg(n, m):
    total = (m + n) // 2
    count = 1
    prev = n
    while prev < m:
        if prev + 1 < m:
            prev += 1
            count += 1
        else:
            break
    if n > m:
        return -1
    if count == 0:
        return '0b0'
    # Calculate the average
    avg = total // count
    # Round to nearest integer and convert to binary
    if avg % 2 == 0:
        return f'0b{avg // 2:b}'
    else:
        return f'0b{avg + 1 // 2:b}'