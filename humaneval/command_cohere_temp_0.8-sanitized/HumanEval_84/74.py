def solve(N):
    bin_str = bin(N)[2:]
    return bin_str.count('1') % 2 == 0 and str(bin_str.count('1')) or '0'