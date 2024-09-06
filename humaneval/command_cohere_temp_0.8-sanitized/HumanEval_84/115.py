def solve(N):
    BIN_DIGIT_VAL = [0, 1]
    SUM_IN_BIN = 0
    DIGITS = [int(d) for d in str(N)]
    
    for digit in DIGITS:
        SUM_IN_BIN += BIN_DIGIT_VAL[digit % 2]
        
        if SUM_IN_BIN > 1:
            return '1'
        
        BIN_DIGIT_VAL.append(BIN_DIGIT_VAL[digit % 2] + BIN_DIGIT_VAL[digit % 2 + 1])
    
    return '0' if SUM_IN_BIN == 0 else '1'