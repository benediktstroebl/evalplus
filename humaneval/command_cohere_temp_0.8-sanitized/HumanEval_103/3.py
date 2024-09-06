def rounded_avg(n, m):
    binary_str = '-1' if n > m else bin(round((n + m) / 2))[2:]
    return binary_str if binary_str not in '01' else '-1'