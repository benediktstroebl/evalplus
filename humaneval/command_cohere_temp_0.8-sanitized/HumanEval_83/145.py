def starts_one_ends(n):
    return sum(int(digit) == 1 for digit in format(n, 'b') if digit == '1')