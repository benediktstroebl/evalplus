def digits(n):
    odd_product = 1
    for digit in str(n)[1:]:
        odd_product *= int(digit)
    return odd_product