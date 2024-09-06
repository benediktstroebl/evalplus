def hex_key(num):
    """
    Counts the number of hexadecimal digits that are primes.
    """
    hex_digits = "0123456789ABCDEF"
    count = 0
    for digit in num:
        if hex_digits.index(digit) in [2, 3, 5, 7, 11, 13]:
            count += 1
    return count