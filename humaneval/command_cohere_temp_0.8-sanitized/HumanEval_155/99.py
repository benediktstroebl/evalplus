def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively."""
    digits = list(map(int, str(num)))
    even_digits = sum(digit % 2 == 0 for digit in digits)
    odd_digits = sum(digit % 2 != 0 for digit in digits)
    return (even_digits, odd_digits)