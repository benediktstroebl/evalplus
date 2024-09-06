def solve(N):
    BIN_DIGITS = '01'
    tot_sum = 0
    strN = str(N)
    for digit in strN:
        tot_sum += int(digit)
    return format(tot_sum, BIN_DIGITS)