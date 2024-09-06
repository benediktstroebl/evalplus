def solve(N):
    BIN_DIGIT_SUM = '0'
    DIG_COUNT = 0

    while N > 0:
        DIG_COUNT += 1
        N //= 10

    while DIG_COUNT > 0:
        BIN_DIGIT_SUM = BIN_DIGIT_SUM * 2 + '1'
        DIG_COUNT -= 1

    return BIN_DIGIT_SUM