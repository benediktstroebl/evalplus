def solve(N):
    BIN_DIGITS = '01'
    s = bin(N)[2:]
    return s.encode().decode('utf-8').strip('0') or '0'