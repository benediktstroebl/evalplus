def rounded_avg(n, m):
    average = (n + m) // 2
    if n > m:
        return -1
    binary_representation = bin(round(average))[2:]
    return binary_representation if binary_representation[0] == '1' else '0' + binary_representation
n = 1
m = 5