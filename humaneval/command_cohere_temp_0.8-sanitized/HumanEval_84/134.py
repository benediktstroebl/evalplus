def solve(N):
    BIN_DIGITS = '01'
    res = bin(sum(int(d) for d in str(N)))[2:]
    return res if res.isdigit() else '0' + res