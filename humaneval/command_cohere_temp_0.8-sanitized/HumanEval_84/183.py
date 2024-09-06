def solve(N):
    BIN_DIGIT_SUM = ''
    total_sum = 0
    
    while N > 0:
        digit = N % 2
        total_sum += digit
        
        BIN_DIGIT_SUM = BIN_DIGIT_SUM + str(digit)
        N //= 2
        
    return BIN_DIGIT_SUM if total_sum == 1 else '1' + BIN_DIGIT_SUM