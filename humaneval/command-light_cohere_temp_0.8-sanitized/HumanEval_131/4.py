def digits(n):
    if not_n(n):
        return 0
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product