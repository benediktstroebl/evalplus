def solve(n):
    bin_sum = 0
    while n > 0:
        digit = n % 10
        bin_sum += digit
        n = n // 10
    return format(bin_sum, 'b')