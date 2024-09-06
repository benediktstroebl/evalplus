def solve(n):
    bin_str = bin(n)[2:]
    sum_str = ''.join(str(int(bit) for bit in bin_str if bit == '1'))
    return sum_str