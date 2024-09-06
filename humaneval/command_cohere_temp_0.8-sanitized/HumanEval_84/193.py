def solve(N):
    binary_str = ''
    total_sum = 0

    while N > 0:
        digit = N % 2
        total_sum += digit
        binary_str = str(digit) + binary_str
        N //= 2

    return f'{total_sum:b}' + binary_str