def digits(n):
    if n == 0:
        return 0
    prod = 1
    for digit in str(n)[1:]:
        prod *= int(digit)
    return prod