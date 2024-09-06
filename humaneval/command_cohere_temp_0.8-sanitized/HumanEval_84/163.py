def solve(N):
    BIN_DIGIT_SUM = ''.join(str(bin(N)[2:]).count('1'))
    return BIN_DIGIT_SUM