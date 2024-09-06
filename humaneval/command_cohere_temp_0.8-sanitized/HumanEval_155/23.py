def even_odd_count(num):
    """Return number of even and odd digits in num."""
    # Check if the number is negative, count it as odd
    num = abs(num)
    odd = 1
    even = 0
    for digit in str(num):
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)