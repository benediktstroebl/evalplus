def solve(N):
    # Compute the sum of digits in binary representation of N
    sum_digits = sum(int(digit) for digit in str(N))
    return '1' + str(sum_digits)