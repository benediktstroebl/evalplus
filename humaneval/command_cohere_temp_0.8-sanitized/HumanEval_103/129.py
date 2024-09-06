def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    binary_representation = bin(round(avg))[2:]
    return binary_representation if binary_representation.isalpha() else "0b" + binary_representation