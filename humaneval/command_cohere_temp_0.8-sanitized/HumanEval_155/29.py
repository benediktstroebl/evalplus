def even_odd_count(num):
    """Return number of even and odd digits in num."""
    digits = str(num)
    even, odd = 0, 0
    for digit in digits:
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd