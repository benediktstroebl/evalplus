def even_odd_count(num):
    """Return number of even and odd digits in num."""
    digits = str(abs(num))
    count_odd = count_even = 0
    for digit in digits:
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd