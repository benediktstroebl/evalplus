def rounded_avg(n, m):
    total = (m + n) // 2
    count = m - n + 1
    if count == 0:
        return '-1'
    rounded_total = round(total)
    binary_representation = bin(rounded_total)[2:]
    return binary_representation if count > 0 else '-1'